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
