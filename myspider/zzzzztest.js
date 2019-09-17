function myfuntion() {
    // var num=0;
    // for (var i = 0; i < 10; i++) {
    //     num+=i
    //     console.log(i)
    // }
    // console.log(num)

    var re = /\d+/g;
    var re1 = /\p{P}+/g
    var teststr='11233,eeee3333';
    var teststr1=',,,:::';
    var res=re.exec(teststr);
    var res1= teststr.match(re)
    var res2 = teststr.replace(re,'ddfdfdf')
    var res3 = re1.test(teststr1)
    console.log(res3)
    console.log(res2)
    console.log(res1)
    console.log(res)

}

myfuntion();