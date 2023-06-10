const fs = require('fs')
fs.readFile('text.txt', 'utf-8', function (err, data) {
        if (err) {
        console.error(err)
        return
    }
    console.log(data);
});

fs.writeFile('text.txt', ("It's a crazy world!"), function (err) {
            if (err) {
        console.error(err)
        return
    }
    else {
        console.log ('written!')
    }
})

fs.appendFile('text1.txt', " Async text added.", function (err) {
    if (err) {
        console.error(err);
        return;
    } else {
        console.log('written more words!');
    }
});
// or like this:
fs.appendFileSync('text1.txt', ' SyncText added.\n');
console.log('Written more words!');

fs.unlink('filetodelete.txt', (err) => {
    console.log('delete complete.');
});


