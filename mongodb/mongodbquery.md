# MongoDB常用查找命令


## lookup
```javascript
db.getCollection('customers').aggregate([
{$match:{"_id" : ObjectId("5b5936841361523ad61921d7"),}},
{$unwind: {path:'$vehicles', preserveNullAndEmptyArrays: true}},
   {
      $lookup:
         {
           from: "maintenances",
           let: { customerId: "$_id", vehicleId: '$vehicles._id'},
           pipeline: [
              { $match:
                 { $expr:
                    { $and:
                       [
                         { $eq: [ "$customerId",  "$$customerId" ] },
                         { $eq: [ "$vehicleId",  "$$vehicleId" ] },
                       ]
                    }
                 }
              },
           ],
           as: "stockdata"
         }
    }
])

```



### 多表混合排序

var orders = Order.aggregate([
    {
            $match: {_id: storeId},
        },
        {
            $lookup: {
                from: "maintenances",
                let: {
                    storeId: storeId,
                },
                pipeline: [
                    {
                        $match: {
                            $expr: {
                                $eq: ['$storeId', '$$storeId'],
                            }
                        }
                    }
                
                ],
                as:'maintenances'
            }
        },
        {
            $lookup: {
                from: "cares",
                let: {
                    storeId: storeId
                },
                pipeline: [
                    {
                        $match: {
                            $expr: {
                                $eq: ['$storeId', '$$storeId']
                            }
                        }
                    }
                
                ],
                as: 'cares'
            }
        },
        {
            $lookup: {
                from: "sales",
                let: {
                    storeId: storeId
                },
                pipeline: [
                    {
                        $match: {
                            $expr: {
                                $eq: ['$storeId', '$$storeId']
                            }
                        }
                    }
                
                ],
                as: 'sales'
            }
        },
        {
            $addFields: {
                "maintenances.orderType": '1',
                "sales.orderType": '2',
                "cares.orderType": '3',
            }
        },
        {
            $project: {
                _id: 0,
                items: {
                    $concatArrays: ['$maintenances', '$cares', '$sales']
                }
            }
        },
        {$unwind: '$items'},
        {
            $replaceRoot: {
                newRoot: '$items'
            }
        },
    ]
])


### 地理空间位置查询与排序

先创建地理空间索引Geospatial Indexes  https://docs.mongodb.com/manual/geospatial-queries/
db.stores.createIndex({"dstCoordinates":"2dsphere"})
数据库迁移必须先做这个，因为是需要依赖这个索引

再进行排序
https://docs.mongodb.com/manual/reference/operator/aggregation/geoNear/#pipe._S_geoNear

db.stores.aggregate([{
	$geoNear: {
        near: { type: "Point", coordinates: [ -73.9667, 40.78 ]  },
        distanceField: "distance",
        num: 2,
		query:{field1: 'condition'},
        spherical: true
     }

}])

需注意的是$geoNear只能放在管道的第一位。

// 判断cond的使用
db.getCollection('stores').aggregate([{
    $project:{
        a: {$cond: [ {$isArray:"$a"}, {$size:"$a"}, 0]}
        }
    
    }])
	
	
	

