const numbers = [5,0,9,1,7,4,2,6,3,8];
console.log(arr.toString());
for (let i=0; i<arr.length; i++) {
    for (let k = 0; arr.length; k++) {
        if (arr[i] > arr[k]) {
            let temp = arr[i];
            arr[i] = arr[k]
            arr[k] = temp;
        }
    }
}
console.log(arr.toString());