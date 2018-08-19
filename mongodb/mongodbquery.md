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