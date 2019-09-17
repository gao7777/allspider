import execjs


# env= execjs.get().name
# print(env)

js_code = """
    function myfuntion(a,b){
    "use strict";
    var res;
    res = a+b;
    return res;
};    
"""

res = execjs.compile(js_code)

num = res.call("myfuntion",1,2)
print(num)