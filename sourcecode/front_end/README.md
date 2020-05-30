## CSS

注释：`/**/`

### 使用css隐藏一个元素

- display: none  元素彻底消失，不触发点击事件
- visibility: hidden  占据页面空间，不触发点击事件
- opacity: 0  设置元素透明度，触发点击事件
- height: 0  

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            width: 100px;
            height: 100px;
            background-color: red;
            margin: 15px;
            padding: 10px;
            border: 5px solid greenyellow;
            display: inline-block;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <div class="none"><h1>None</h1></div>
    <div class="hidden"><h1>hidden</h1></div>
    <div class="opaity0"><h1>opaity0</h1></div>
    <div class="height0"><h1>height0</h1></div>
</body>
<script src="jquery-3.5.1.min.js"></script>
<script>
    $(".none").on("click", function () {
        console.log("none clicked");
    })
    $(".hidden").on("click", function () {
        console.log("hidden clicked");
    })
    $(".opaity0").on("click", function () {
        console.log("opaity0 clicked");
    })
    $(".height0").on("click", function () {
        console.log("height0 clicked");
    })
</script>
</html>
```

显示效果：

![image-20200530145121628](https://i.loli.net/2020/05/30/b79TLWyIBP126HS.png)

在style标签中添加以下内容：

```css
.none {display: none;}
.hidden {visibility: hidden;}
.opaity0 {opacity: 0;}
.height0 {height: 0;}
```

![image-20200530145647479](https://i.loli.net/2020/05/30/I2ojUzOdc7hP6SF.png)

可以看出 `display:none`是彻底的没了，元素彻底消失，不会触发点击事件；

`visibility: hidden`是看不见的，也不会触发点击事件，但是还会占据页面空间

`opacity: 0`只是将元素设置为透明，依然可以触发点击事件

`height: 0`将元素的高度设置为0，并且设置 `overflow:hidden`[^1] ; 如果元素设置了border、padding等属性，很显然页面上还是可以看到，也是可以触发点击事件的；如果这些属性都设置为0，这个元素相当于消失了，即无法触发点击事件

![image-20200530202604438](https://i.loli.net/2020/05/30/hDVjqH8QacpxJ7l.png)

[^1]: 隐藏超出的内容