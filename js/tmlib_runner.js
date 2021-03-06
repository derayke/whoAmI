// forked from phi's "tmlib.js examples - Magic Square" http://jsdo.it/phi/b1p8
// forked from phi's "tmlib.js template" http://jsdo.it/phi/jko1

/*
 * phi
 */


/*
 * 定数
 */

var SCREEN_WIDTH    = Math.max(screen.width, screen.height);
var SCREEN_HEIGHT   = Math.max(screen.width, screen.height);


/**
 * 魔方陣クラス
 */
var MagicSquareSprite = tm.createClass({
    
    superClass: tm.app.Sprite,
    
    init: function() {
        this.superInit(250, 250);
        
        this.radius    = 80;
        this.blendMode = "lighter";
        
        this.setupAnim();
        this.rendererCanvas();
    },
    
    setupAnim: function() {
        this.animation.addTween({
            prop: "alpha",
            begin: 0,
            finish: 1.0,
            duration: 1000,
        });
        this.animation.addTween({
            prop: "rotation",
            begin: 0,
            finish: 360,
            duration: 1000,
            func: "easeInOutQuad",
        });
        
        this.animation.addTween({
            prop: "scaleX",
            begin: 1.0,
            finish: 2.0,
            duration: 1000,
            delay: 1500,
            func: "easeInOutBack",
        });
        this.animation.addTween({
            prop: "scaleY",
            begin: 1.0,
            finish: 2.0,
            duration: 1000,
            delay: 1500,
            func: "easeInOutBack",
        });
        this.animation.addTween({
            prop: "alpha",
            begin: 1.0,
            finish: 0.0,
            duration: 1000,
            delay: 1500,
        });
        
        this.onanimationend = function() {
            this.remove();
        };
    },
    
    
    rendererCanvas: function() {
        var canvas = this.canvas;
        var hue    = tm.util.Random.randint(0, 360);
        var hsl    = "hsl({0}, 75%, 50%)".format(hue);
        
        canvas.setTransformCenter();
        canvas.fillStyle  = hsl;
        canvas.strokeStyle= hsl;
        // 星
        canvas.lineWidth = 2;
        canvas.strokeStar(0, 0, this.radius, 6);
        canvas.lineWidth = 1;
        // ５角形
        canvas.strokePolygon(0, 0, this.radius, 6);
        // 円
        canvas.strokeCircle(0, 0, this.radius);
        // 内側の円
        canvas.strokeCircle(0, 0, this.radius);
        canvas.lineWidth = 4;
        // 外側の円
        canvas.strokeCircle(0, 0, this.radius*1.35);
        
        var text = "好棒棒*好棒棒*好棒棒*好棒棒*好棒棒*好棒棒*好棒棒*好棒棒*好棒棒*";
        canvas.lineWidth = 1;
        for (var i=0,len=text.length; i<len; ++i) {
            canvas.save();
            canvas.rotate(Math.degToRad(i*10));
            canvas.translate(0, -this.radius*1.1);
            canvas.fillText(text[i], 0, 0);
            canvas.restore();
        }
    },

});

var app
tm.main(function() {
    app = tm.app.CanvasApp("#world");
    app.width = window.innerWidth;
    app.height = window.innerHeight;
    // app.resize(screen.availWidth, screen.availHeight);
    app.fitWindow();
    //app.enableStats();
    app.background = "rgba(0, 0, 0, 0.25)";
    
    app.currentScene.name = "hoge";
    app.currentScene.onmousedown = function(e) {
        var p  = e.app.pointing;
        var ms = MagicSquareSprite();
        ms.x = p.x;
        ms.y = p.y;
        ms.addChildTo(this);
    };
    
    // あらかじめいくつか生成しておく
     for (var i=0; i<20; ++i) {
         var ms = MagicSquareSprite();
        ms.x = tm.util.Random.randint(0, SCREEN_WIDTH);
         ms.y = tm.util.Random.randint(0, SCREEN_HEIGHT);;
         ms.addChildTo(app.currentScene);
     }
    
    app.update = function() {
        var scene = this.currentScene;
        var key = this.keyboard;
        if (key.getKeyDown("space") == true) {
            (scene.isUpdate == true) ? scene.sleep() : scene.wakeUp();
        }
    }
    
    // mdlclick でキャプチャ
    tm.dom.Element(app.getElement()).event.mdlclick(function() {
        app.canvas.saveAsImage();
    });    
});
