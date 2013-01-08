//>>built
define("dojox/widget/Loader",["dijit","dojo","dojox","dojo/require!dijit/_Widget,dijit/_Templated"],function(_1,_2,_3){
_2.provide("dojox.widget.Loader");
_2.deprecated("dojox.widget.Loader","","2.0");
_2.require("dijit._Widget");
_2.require("dijit._Templated");
_2.declare("dojox.widget.Loader",[_1._Widget,_1._Templated],{loadIcon:_2.moduleUrl("dojox.widget.Loader","icons/loading.gif"),loadMessage:"Loading ...",hasVisuals:true,attachToPointer:true,duration:125,_offset:16,_pointerConnect:null,_xhrStart:null,_xhrEnd:null,templateString:"<div dojoAttachPoint=\"loadNode\" class=\"dojoxLoader\">"+"<img src=\"${loadIcon}\" class=\"dojoxLoaderIcon\"> <span dojoAttachPoint=\"loadMessageNode\" class=\"dojoxLoaderMessage\"></span>"+"</div>",postCreate:function(){
if(!this.hasVisuals){
this.loadNode.style.display="none";
}else{
if(this.attachToPointer){
_2.removeClass(this.loadNode,"dojoxLoader");
_2.addClass(this.loadNode,"dojoxLoaderPointer");
}
this._hide();
}
this._setMessage(this.loadMessage);
this._xhrStart=this.connect(_2,"_ioSetArgs","_show");
this._xhrEnd=this.connect(_2.Deferred.prototype,"_fire","_hide");
},_setMessage:function(_4){
this.loadMessageNode.innerHTML=_4;
},_putLoader:function(e){
_1.placeOnScreen(this.loadNode,{x:e.clientX+this._offset,y:e.clientY+this._offset},["TL","BR"]);
},_show:function(){
_2.publish("Loader",[{message:"started"}]);
if(this.hasVisuals){
if(this.attachToPointer){
this._pointerConnect=this.connect(document,"onmousemove","_putLoader");
}
_2.style(this.loadNode,{opacity:0,display:""});
_2.fadeIn({node:this.loadNode,duration:this.duration}).play();
}
},_hide:function(){
_2.publish("Loader",[{message:"ended"}]);
if(this.hasVisuals){
if(this.attachToPointer){
this.disconnect(this._pointerConnect);
}
_2.fadeOut({node:this.loadNode,duration:this.duration,onEnd:_2.partial(_2.style,this.loadNode,"display","none")}).play();
}
}});
});