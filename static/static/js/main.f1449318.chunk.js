(this["webpackJsonpattendance-app"]=this["webpackJsonpattendance-app"]||[]).push([[0],{111:function(e,t,a){},112:function(e,t,a){"use strict";a.r(t);var n=a(1),c=a.n(n),l=a(24),r=a.n(l);a(81),Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a(82),a(0);var o=a(13),i=a(7),u=a(46),m=a.n(u),s=a(61),d=a(22),E=a(10),f=a(62),h=a(118),p=a(114),b=a(122),v=a(115),g=a(72),j=a(119),O=a(123),w=a(116),k=a(124),y=a(73),N=a(50),x=a(45),S=a(64),C=a.n(S),T=a(42),I=a.n(T),B=a(120),L=a(121);var D,H,M,A,R=function(e){return c.a.createElement("div",null,c.a.createElement(B.a,{bg:"light",className:"mb-2"},c.a.createElement(p.a,null,c.a.createElement(L.a,{className:"ml-auto"},c.a.createElement(L.a.Link,null,c.a.createElement(o.b,{to:"/"},"Home")),c.a.createElement(L.a.Link,null,c.a.createElement(o.b,{to:"/classes"},"C\xe1c l\u1edbp c\u1ee7a t\xf4i")),c.a.createElement(L.a.Link,null,c.a.createElement(o.b,{to:"/login"},"Logout"))))))},z=window.AudioContext||window.webkitAudioContext,F=window.Recorder;function J(){navigator.mediaDevices.getUserMedia({audio:!0,video:!1}).then((function(e){console.log("stream created"),D=new z,H=e,A=D.createMediaStreamSource(e),console.log(A),(M=new F(A,{numChannels:1})).record(),console.log("Recording started")}))}function P(e){console.log("stopButton clicked"),M.stop(),H.getAudioTracks()[0].stop(),M.exportWAV((function(t){return e(t)}))}var V=a(30),G=a.n(V);function W(){var e=Object(f.a)(["\n    display: block;\n    margin: auto;\n    border-color: #007bff;\n"]);return W=function(){return e},e}var U=Object(x.css)(W());var Y=function(e){var t=Object.assign({},e),a=t.match.params.id,l=Object(n.useState)(!1),r=Object(E.a)(l,2),i=r[0],u=r[1],f=Object(n.useState)(!1),x=Object(E.a)(f,2),S=x[0],T=x[1],B=Object(n.useState)(""),L=Object(E.a)(B,2),D=L[0],H=L[1];Object(n.useEffect)((function(){G.a.get(""+"/api/get-students?classId=".concat(a)).then((function(e){e.data&&F(e.data.map((function(e){return{id:e[0],name:e[1],attendant:!1,show:!0}})))}))}),[]);var M=Object(n.useState)([]),A=Object(E.a)(M,2),z=A[0],F=A[1],V=Object(n.useState)(z[0]),W=Object(E.a)(V,2),Y=W[0],K=W[1];Object(n.useEffect)((function(){F(z.map((function(e){var t=new RegExp("".concat(D),"g");return e.name.match(t)||e.id.toString().match(t)?Object(d.a)(Object(d.a)({},e),{},{show:!0}):Object(d.a)(Object(d.a)({},e),{},{show:!1})})))}),[D]);var $=function(){var e=Object(s.a)(m.a.mark((function e(){var t;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:t=function(e,t){var a=0;!function n(){a<e.length&&t(e[a++]).then(n)}()},z.map((function(e){return function(){return q(e)}})),t(z,q);case 3:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),_=function(){return u(!1)},q=function(e){var t=window.responsiveVoice;return K(e),u(!0),new Promise((function(a,n){var c;J(),setTimeout((function(){P((function(n){c=n,t.speak("B\u1ea1n "+e.name+" c\xf3 m\u1eb7t kh\xf4ng","Vietnamese Male",{onend:function(){J(),T(!0),setTimeout((function(){T(!1),P((function(t){!function(e,t,a,n){console.log(e);var c=new FormData;c.append("file",e),c.append("noise",t),c.append("name",a),fetch("http://localhost:5000/api/check-attendance",{method:"POST",body:c}).then((function(e){e.json().then((function(e){n&&n(e)})).catch((function(e){alert("Error!")}))}))}(t,c,e.name,(function(t){"success"===t.status?I.a.fire({title:"Th\xe0nh c\xf4ng",text:"".concat(e.name," \u0111\xe3 c\xf3 m\u1eb7t"),icon:"success"}).then((function(t){var n;t.value;n=e.id,F(z.map((function(e){return e.id===n?Object(d.a)(Object(d.a)({},e),{},{attendant:!0}):e}))),_(),a(!0)})):I.a.fire({title:"Th\u1ea5t b\u1ea1i",text:"".concat(e.name," Kh\xf4ng c\xf3 m\u1eb7t"),icon:"error"}).then((function(e){e.value;_(),a(!1)}))}))}))}),3e3)}})}))}),2e3)}))};return c.a.createElement("div",{className:"App"},c.a.createElement(R,null),c.a.createElement(h.a,{show:i,onHide:_},c.a.createElement(h.a.Body,null,Y&&c.a.createElement("p",null,Y.name),S?c.a.createElement("p",null,"Recording..."):null,c.a.createElement(C.a,{css:U,size:10,color:"#123abc",loading:S}))),c.a.createElement(p.a,null,c.a.createElement(b.a,null,c.a.createElement(b.a.Item,{href:"#/classes"},"Home"),c.a.createElement(b.a.Item,null,c.a.createElement(o.b,{to:"/class-transaction/".concat(a)},a)),c.a.createElement(b.a.Item,{active:!0},"T\u1ea1o m\u1edbi bu\u1ed5i \u0111i\u1ec3m danh")),c.a.createElement(v.a,{className:"mb-5"},c.a.createElement(g.a,{md:8},c.a.createElement(j.a.Row,{className:"mb-3"},c.a.createElement(g.a,{className:"d-flex align-items-center justify-content-around"},c.a.createElement(y.BsSearch,{size:"1.5em",className:"mr-3"}),c.a.createElement(j.a.Control,{type:"text",placeholder:"Search here",onChange:function(e){H(e.target.value),setTimeout((function(){}),100)}}))),c.a.createElement("div",{className:"list-box"},c.a.createElement(O.a,null,z.length>0?z.filter((function(e){return!e.attendant})).filter((function(e){return e.show})).map((function(e){return c.a.createElement(O.a.Item,{key:e.id},c.a.createElement("div",{className:"title-group"},c.a.createElement("div",{className:"l-title"},e.name),c.a.createElement("div",{className:"l-description"},e.id)),c.a.createElement("div",{className:"float-right clearfix"},c.a.createElement(w.a,{variant:"outline-success",onClick:function(){q(e)}},"check")))})):c.a.createElement("p",null,"Tr\u1ed1ng"))),c.a.createElement(w.a,{className:"mt-2",color:"success",onClick:$},"\u0110i\u1ec3m danh t\u1ef1 \u0111\u1ed9ng"),c.a.createElement(w.a,{className:"mt-2 ml-2",color:"success",onClick:function(){var e=JSON.stringify();console.log(e),G.a.post("/api/add-class-transaction",{detail:z.map((function(e){return{id:e.id,name:e.name,attendant:e.attendant}})),date:new Date,classId:a}).then((function(e){I.a.fire({title:"success"===e.data?"Th\xe0nh c\xf4ng":"Th\u1ea5t b\u1ea1i",text:"success"===e.data?"Th\xf4ng tin bu\u1ed5i \u0111i\u1ec3m danh \u0111\xe3 \u0111\u01b0\u1ee3c ghi l\u1ea1i":"C\xf3 l\u1ed7i x\u1ea3y ra",icon:"success"===e.data?"success":"error"}).then((function(e){e.value&&t.history.push("/class-transaction/"+a)}))}))}},"Save")),c.a.createElement(g.a,{md:4},c.a.createElement(k.a,null,c.a.createElement(k.a.Header,null,"Sinh vi\xean c\xf3 m\u1eb7t"),c.a.createElement(k.a.Body,null,c.a.createElement("div",{className:"l-list"},z.filter((function(e){return e.attendant})).map((function(e){return c.a.createElement("div",{key:e.id,className:"l-item"},c.a.createElement(N.a,{color:"green",size:"1.3em",className:"mr-2"}),c.a.createElement("span",null,e.name),c.a.createElement("div",{className:"float-right"},c.a.createElement(N.b,{size:"1.5em",color:"red",cursor:"pointer",onClick:function(){return t=e.id,void F(z.map((function(e){return e.id===t?Object(d.a)(Object(d.a)({},e),{},{attendant:!1}):e})));var t}})))})))))))))};var K=function(e){return c.a.createElement("div",{className:"bg-image d-flex justify-content-center align-items-center"},c.a.createElement("div",{className:"form-box"},c.a.createElement(j.a.Group,null,c.a.createElement(j.a.Label,null,"Username"),c.a.createElement(j.a.Control,{name:"uname"})),c.a.createElement(j.a.Group,null,c.a.createElement(j.a.Label,null,"Password"),c.a.createElement(j.a.Control,{name:"password",type:"password"})),c.a.createElement(w.a,{onClick:function(){e.history.push("/classes")}},"Submit")))};a(111);var $=function(){var e=function(e){var t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],a=Object(n.useState)(!1),c=Object(E.a)(a,2),l=c[0],r=c[1],o=Object(n.useState)(null),i=Object(E.a)(o,2),u=i[0],m=i[1],s=Object(n.useState)(null),d=Object(E.a)(s,2),f=d[0],h=d[1],p=Object(n.useCallback)((function(){return r(!0),m(null),h(null),e().then((function(e){return m(e)})).catch((function(e){return h(e)})).finally((function(){return r(!1)}))}),[e]);return Object(n.useEffect)((function(){t&&p()}),[p,t]),[p,l,u,f,m]}((function(){return new Promise((function(e,t){fetch("/api/get-classes",{method:"GET"}).then((function(t){t.json().then((function(t){e(t)}))})).catch((function(e){return t(e)}))}))}),!1),t=Object(E.a)(e,4),a=t[0],l=(t[1],t[2]);return t[3],Object(n.useEffect)((function(){a()}),[]),c.a.createElement("div",null,c.a.createElement(R,null),c.a.createElement(p.a,null,l?c.a.createElement(v.a,null,l.map((function(e){return c.a.createElement(g.a,{md:4,key:e[0]},c.a.createElement(k.a,null,c.a.createElement(k.a.Img,{variant:"top",src:e[2]}),c.a.createElement(k.a.Title,null,c.a.createElement(o.b,{to:"/class-transaction/".concat(e[0])},e[0])),c.a.createElement(k.a.Text,null,e[1])))}))):c.a.createElement("div",null,"null")))},_=a(74),q=a(117);var Q=function(e){var t=e.match,a=(Object(_.a)(e,["match"]),t.params.id),l=Object(n.useState)([]),r=Object(E.a)(l,2),i=r[0],u=r[1],m=Object(n.useState)(!1),s=Object(E.a)(m,2),d=s[0],f=s[1],b=Object(n.useState)(null),v=Object(E.a)(b,2),g=v[0],j=v[1];return Object(n.useEffect)((function(){G.a.get("/api/get-class-transaction?classId="+a).then((function(e){u(e.data.map((function(e){return{id:e[0],date:new Date(e[1]),classId:e[2],detail:JSON.parse(e[3])}})))}))}),[]),c.a.createElement("div",null,c.a.createElement(R,null),c.a.createElement(h.a,{show:d,onHide:function(){return f(!1)}},g),c.a.createElement(p.a,null,c.a.createElement("h3",null,"L\u1ecbch s\u1eed \u0111i\u1ec3m danh"),c.a.createElement(O.a,null,i.map((function(e){return c.a.createElement(O.a.Item,{key:e.id,action:!0,onClick:function(){return function(e){j(c.a.createElement(n.Fragment,null,c.a.createElement(h.a.Header,{closeButton:!0},c.a.createElement(h.a.Title,null,"\u0110i\u1ec3m danh ng\xe0y ",e.date.getDate(),"/",e.date.getMonth(),"/",e.date.getFullYear())),c.a.createElement(h.a.Body,null,c.a.createElement("div",null,c.a.createElement(q.a,{striped:!0,bordered:!0,hover:!0},c.a.createElement("thead",null,c.a.createElement("tr",null,c.a.createElement("th",null,"mssv"),c.a.createElement("th",null,"Name"),c.a.createElement("th",null,"C\xf3 m\u1eb7t"))),c.a.createElement("tbody",null,e.detail.map((function(e){return c.a.createElement("tr",{key:e.id},c.a.createElement("td",null,e.id),c.a.createElement("td",null,e.name),c.a.createElement("td",null,e.attendant?"C\xf3 m\u1eb7t":"V\u1eafng"))}))),c.a.createElement("a",{target:"_blank",rel:"noopener noreferrer",href:"".concat("","/attendant-csv/").concat(e.id)},c.a.createElement(w.a,{className:"mt-2"},"Export Excel"))))))),f(!0)}(e)}},e.classId," - ",e.date.getDate(),"/",e.date.getMonth(),"/",e.date.getFullYear())}))),c.a.createElement(O.a,{className:"mt-3"},c.a.createElement(O.a.Item,{action:!0,variant:"primary"},c.a.createElement(o.b,{to:"/class/".concat(a)},"+ \u0110i\u1ec3m danh h\xf4m nay")))))};var X=function(e){return c.a.createElement("div",null,c.a.createElement(i.d,null,c.a.createElement(i.b,{exact:!0,path:"/",render:function(){return c.a.createElement(i.a,{to:"/login"})}}),c.a.createElement(i.b,{exact:!0,path:"/class/:id",component:Y}),c.a.createElement(i.b,{exact:!0,path:"/class-transaction/:id",component:Q}),c.a.createElement(i.b,{exact:!0,path:"/classes",component:$}),c.a.createElement(i.b,{path:"/login",component:K})))};r.a.render(c.a.createElement(c.a.StrictMode,null,c.a.createElement(o.a,null,c.a.createElement(X,null))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))},76:function(e,t,a){e.exports=a(112)},81:function(e,t,a){}},[[76,1,2]]]);
//# sourceMappingURL=main.f1449318.chunk.js.map