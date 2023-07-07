import{d as m,b as f,e as u,o as b,c as g,a as t,f as c,w as p,v as h,u as s,t as _,g as P,F as V,h as w}from"./index-2106a6ea.js";const z=m("path",{state:()=>({la_a:"",lo_a:"",la_b:"",lo_b:"",distance:"",arc_distance:"",az_a_b:"",az_b_a:"",p_a_elevation:"",p_b_elevation:"",graph:"",changed:!1}),actions:{async calculate(){const e=parseInt(this.la_a*1e6,10),i=parseInt(this.lo_a*1e6,10),d=parseInt(this.la_b*1e6,10),r=parseInt(this.lo_b*1e6,10);try{const a=await f.get(`/profile/${e}/${i}/${d}/${r}`);this.distance=a.data.distance,this.az_a_b=a.data.az_a_b,this.az_b_a=a.data.az_b_a,this.p_a_elevation=a.data.p_a_elevation,this.p_b_elevation=a.data.p_b_elevation,this.graph=a.data.graph,this.changed=!0}catch(a){alert(a)}}}}),B=t("h3",null,"Find all points and their elevations between the given ones every 10 meters",-1),L=t("legend",null,"Point A",-1),A={class:"grid"},$={for:"la_a"},x={for:"lo_a"},C=t("legend",null,"Point B",-1),k={class:"grid"},y={for:"la_b"},I={for:"lo_b"},N={key:0,class:"answer"},U=["src"],D={__name:"ComponentPath",setup(v){const e=z(),i=u({get(){return e.la_a},set(o){e.la_a=o,e.changed=!1}}),d=u({get(){return e.la_b},set(o){e.la_b=o,e.changed=!1}}),r=u({get(){return e.lo_a},set(o){e.lo_a=o,e.changed=!1}}),a=u({get(){return e.lo_b},set(o){e.lo_b=o,e.changed=!1}});return(o,l)=>(b(),g(V,null,[B,t("fieldset",null,[L,t("div",A,[t("label",$,[c(" Latitude "),p(t("input",{id:"la_a","onUpdate:modelValue":l[0]||(l[0]=n=>i.value=n),placeholder:"Latitude"},null,512),[[h,i.value]])]),t("label",x,[c(" Longitude "),p(t("input",{id:"lo_a","onUpdate:modelValue":l[1]||(l[1]=n=>r.value=n),placeholder:"Longitude"},null,512),[[h,r.value]])])])]),t("fieldset",null,[C,t("div",k,[t("label",y,[c(" Latitude "),p(t("input",{id:"la_b","onUpdate:modelValue":l[2]||(l[2]=n=>d.value=n),placeholder:"Latitude"},null,512),[[h,d.value]])]),t("label",I,[c(" Longitude "),p(t("input",{id:"lo_b","onUpdate:modelValue":l[3]||(l[3]=n=>a.value=n),placeholder:"Longitude"},null,512),[[h,a.value]])])])]),t("button",{onClick:l[4]||(l[4]=n=>s(e).calculate())},"Calculate"),s(e).changed?(b(),g("div",N,[t("fieldset",null,[t("ul",null,[t("li",null,"Distance between two points in kilometers in a straight line "+_(s(e).distance),1),t("li",null,"Cource from Point A to Point B "+_(s(e).az_a_b)+"°",1),t("li",null,"Cource from Point B to Point A "+_(s(e).az_b_a)+"°",1),t("li",null,"Point A. Altitude "+_(s(e).p_a_elevation)+" m",1),t("li",null,"Point B. Altitude "+_(s(e).p_b_elevation)+" m",1)])]),t("img",{alt:"Profile PointA to PointB",src:s(e).graph},null,8,U)])):P("",!0)],64))}},F={class:"grid"},T={__name:"ViewPath",setup(v){return document.title="Georgaphical path",(e,i)=>(b(),g("div",F,[t("div",null,[w(D)])]))}};export{T as default};