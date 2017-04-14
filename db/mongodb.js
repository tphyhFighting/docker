use runoob
// db.col.insert({title: 'MongoDB 教程', 
//     description: 'MongoDB 是一个 Nosql 数据库',
//     by: '菜鸟教程',
//     url: 'http://www.runoob.com',
//     tags: ['mongodb', 'database', 'NoSQL'],
//     likes: 100
// })
// db.col.find()
// db.col.find(
//    {
//     "by":"菜鸟教程",
//     "title":"MongoDB 教程"   
//    }
// 
// ).pretty()
// db.col.find(
//    {
//       $or: [
// 	    {"title":"MongoDB 教程"},
//             {"by":"Runoob"}
//       ]
//    }
// ).pretty()
// where likes > 50 and (by = "菜鸟教程" or title = "MongoDB 教程")
// db.col.find({"likes": {$gt:50}, $or: [{"by": "菜鸟教程"},{"title": "MongoDB 教程"}]}).pretty()
// db.col.find({"title" : {$type : 2}}).limit(10).skip(0)
db.col.find({"title" : {$type : 2}}).limit(10).skip(1)