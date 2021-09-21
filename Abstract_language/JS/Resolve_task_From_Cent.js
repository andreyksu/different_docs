//Есть входной массив данных, нужно получить выходной массив данных.
//Отсутстувует toLowerCase() - нужно добавить.


data = { "a": 1, "b": -1, "c": "Abc", "d": -5, "e": "ebc", "f": 10, "g": 5, "h": "abc", "k": "абв" }
expected = { "f": 10, "g": 5, "a": 1, "b": -1, "d": -5, "h": "abc", "c": "Abc", "e": "ebc", "k": "абв" }

********************************************************

vArr = Object.keys(data).sort((aa, bb) => {
  a = data[aa];
  b = data[bb];
  if (typeof(a) == "number" && typeof(b) == "number") {
    return -(a - b);
  }
  if (typeof(a) == "number" && typeof(b) == "string") {
    return -1;
  }
  if (typeof(a) == "string" && typeof(b) == "number") {
    return 1;
  }
  if (typeof(a) == "string" && typeof(b) == "string") {
    if (a > b)
      return 1;
    if (a < b)
      return -1;
    return 0;
  }
})
var obj = {}
for (i in vArr) {
  obj[vArr[i]] = data[vArr[i]];
}
console.log(obj);

********************************************************
var str = [];
var number = [];
Object.entries(data).forEach(
  elem => {
    if (typeof(elem[1]) === "number")
      number.push(elem);
    else if (typeof(elem[1]) === "string")
      str.push(elem);
  }
)
str.sort((first, second) => {
  return first[1] > second[1] ? 1 : first[1] < second[1] ? -1 : 0;
});
number.sort((first, second) => {
  return first[1] - second[1];
});
var result = number.concat(str);
var resObj = {};
result.forEach(elem => {
  resObj[elem[0]] = elem[1];
});
console.log(res);

******************************************************** На 100 процентов соответствует предыдущей реализации
var str = [];
var number = [];
var res= {};
Object.entries(data).forEach(elem => {
if (typeof(elem[1])==="number")
	number.push(elem);
else if (typeof(elem[1])==="string")
	str.push(elem);
})

number.sort((first, second)=>{return first[1] - second[1];}).concat(str.sort((first, second)=>{return first[1] > second[1] ? 1 : first[1] < second[1] ? -1 : 0;})).forEach(elem=>{res[elem[0]]=elem[1];});

