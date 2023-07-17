import{d as m,b as f,e as c,o as v,c as g,a as t,f as b,w as h,v as p,u as o,t as d,g as $,F as w,h as j}from"./index-c725121e.js";const x=m("distance",{state:()=>({job_id:"",job_status:"",job_poolinterval:"",la_a:"",lo_a:"",la_b:"",lo_b:"",distance:"",arc_distance:"",az_a_b:"",az_b_a:"",p_a_elevation:"",p_b_elevation:"",changed:!1}),actions:{async get_job_status(){try{const e=await f.get(`/distance_check/${this.job_id}`);this.job_status=e.data.job_status,this.changed=!0,this.job_status==="finished"&&(clearInterval(this.job_poolinterval),this.distance=e.data.distance,this.arc_distance=e.data.arc_distance,this.az_a_b=e.data.az_a_b,this.az_b_a=e.data.az_b_a,this.p_a_elevation=e.data.p_a_elevation,this.p_b_elevation=e.data.p_b_elevation)}catch(e){alert(e)}},async calculate(){this.distance="",this.arc_distance="",this.az_a_b="",this.az_b_a="",this.p_a_elevation="",this.p_b_elevation="";const e=1e6,a=parseInt(this.la_a*e,10),_=parseInt(this.lo_a*e,10),u=parseInt(this.la_b*e,10),r=parseInt(this.lo_b*e,10);try{const l=await f.get(`/distance_add_task/${a}/${_}/${u}/${r}`);this.job_id=l.data.job_id,this.job_status=l.data.job_status,this.changed=!0,this.job_status!=="finished"?(this.job_poolinterval=setInterval(()=>{this.get_job_status()},1e3),setTimeout(()=>{clearInterval(this.job_poolinterval)},6e4)):(this.distance=l.data.distance,this.arc_distance=l.data.arc_distance,this.az_a_b=l.data.az_a_b,this.az_b_a=l.data.az_b_a,this.p_a_elevation=l.data.p_a_elevation,this.p_b_elevation=l.data.p_b_elevation)}catch(l){alert(l)}}}}),z=t("h3",null,"Find distance and bearing between two points",-1),I=t("legend",null,"Point A",-1),L={class:"grid"},P={for:"la_a"},V={for:"lo_a"},k=t("legend",null,"Point B",-1),y={class:"grid"},C={for:"la_b"},A={for:"lo_b"},B={key:0,class:"answer"},D={__name:"ComponentDistance",setup(e){const a=x(),_=c({get(){return a.la_a},set(n){a.la_a=n,a.changed=!1}}),u=c({get(){return a.la_b},set(n){a.la_b=n,a.changed=!1}}),r=c({get(){return a.lo_a},set(n){a.lo_a=n,a.changed=!1}}),l=c({get(){return a.lo_b},set(n){a.lo_b=n,a.changed=!1}});return(n,s)=>(v(),g(w,null,[z,t("fieldset",null,[I,t("div",L,[t("label",P,[b(" Latitude "),h(t("input",{id:"la_a","onUpdate:modelValue":s[0]||(s[0]=i=>_.value=i),placeholder:"Latitude"},null,512),[[p,_.value]])]),t("label",V,[b(" Longitude "),h(t("input",{id:"lo_a","onUpdate:modelValue":s[1]||(s[1]=i=>r.value=i),placeholder:"Longitude"},null,512),[[p,r.value]])])])]),t("fieldset",null,[k,t("div",y,[t("label",C,[b(" Latitude "),h(t("input",{id:"la_b","onUpdate:modelValue":s[2]||(s[2]=i=>u.value=i),placeholder:"Latitude"},null,512),[[p,u.value]])]),t("label",A,[b(" Longitude "),h(t("input",{id:"lo_b","onUpdate:modelValue":s[3]||(s[3]=i=>l.value=i),placeholder:"Longitude"},null,512),[[p,l.value]])])])]),t("button",{onClick:s[4]||(s[4]=i=>o(a).calculate())},"Calculate"),o(a).changed?(v(),g("div",B,[t("fieldset",null,[t("ul",null,[t("li",null,"Distance between two points in kilometers in a straight line "+d(o(a).distance),1),t("li",null,"Distance between two points in kilometers on the surface of the planet "+d(o(a).arc_distance),1),t("li",null,"Cource from Point A to Point B "+d(o(a).az_a_b)+"°",1),t("li",null,"Cource from Point B to Point A "+d(o(a).az_b_a)+"°",1),t("li",null,"Point A. Altitude "+d(o(a).p_a_elevation)+" m",1),t("li",null,"Point B. Altitude "+d(o(a).p_b_elevation)+" m",1)])])])):$("",!0)],64))}},U=m("nextpoint",{state:()=>({job_id:"",job_status:"",job_poolinterval:"",la_a:"",lo_a:"",la_b:"",lo_b:"",dis:"",bea:"",p_a_elevation:"",p_b_elevation:"",changed:!1}),actions:{async get_job_status(){try{const e=await f.get(`/nextpoint_check/${this.job_id}`);this.job_status=e.data.job_status,this.changed=!0,this.job_status==="finished"&&(clearInterval(this.job_poolinterval),this.la_b=e.data.latitude_b,this.lo_b=e.data.longitude_b,this.p_a_elevation=e.data.p_a_elevation,this.p_b_elevation=e.data.p_b_elevation)}catch(e){alert(e)}},async calculate(){this.la_b="",this.lo_b="",this.p_a_elevation="",this.p_b_elevation="";const e=1e6,a=parseInt(this.la_a*e,10),_=parseInt(this.lo_a*e,10),u=parseInt(this.dis*e,10),r=parseInt(this.bea*e,10);try{const l=await f.get(`/nextpoint_add_task/${a}/${_}/${u}/${r}`);this.job_id=l.data.job_id,this.job_status=l.data.job_status,this.changed=!0,this.job_status!=="finished"?(this.job_poolinterval=setInterval(()=>{this.get_job_status()},1e3),setTimeout(()=>{clearInterval(this.job_poolinterval)},6e4)):(this.la_b=l.data.latitude_b,this.lo_b=l.data.longitude_b,this.p_a_elevation=l.data.p_a_elevation,this.p_b_elevation=l.data.p_b_elevation)}catch(l){alert(l)}}}}),N=t("h3",null,"Find next point by distance and bearing ",-1),F=t("legend",null,"Point A",-1),S={class:"grid"},T={for:"la_a"},E={for:"lo_a"},M={for:"dis"},q={for:"bea"},G={key:0,class:"answer"},H=t("legend",null,"Point A",-1),J=t("legend",null,"Point B",-1),K={__name:"ComponentNextPoint",setup(e){const a=U(),_=c({get(){return a.la_a},set(n){a.la_a=n,a.changed=!1}}),u=c({get(){return a.lo_a},set(n){a.lo_a=n,a.changed=!1}}),r=c({get(){return a.dis},set(n){a.dis=n,a.changed=!1}}),l=c({get(){return a.bea},set(n){a.bea=n,a.changed=!1}});return(n,s)=>(v(),g(w,null,[N,t("fieldset",null,[F,t("div",S,[t("label",T,[b(" Latitude "),h(t("input",{id:"la_a","onUpdate:modelValue":s[0]||(s[0]=i=>_.value=i),placeholder:"Latitude"},null,512),[[p,_.value]])]),t("label",E,[b(" Longitude "),h(t("input",{id:"lo_a","onUpdate:modelValue":s[1]||(s[1]=i=>u.value=i),placeholder:"Longitude"},null,512),[[p,u.value]])]),t("label",M,[b(" Distance "),h(t("input",{id:"dis","onUpdate:modelValue":s[2]||(s[2]=i=>r.value=i),placeholder:"Distance"},null,512),[[p,r.value]])]),t("label",q,[b(" Bearing (°) "),h(t("input",{id:"bea","onUpdate:modelValue":s[3]||(s[3]=i=>l.value=i),placeholder:"Bearing (°)"},null,512),[[p,l.value]])])])]),t("button",{onClick:s[4]||(s[4]=i=>o(a).calculate())},"Calculate"),o(a).changed?(v(),g("div",G,[t("fieldset",null,[H,t("ul",null,[t("li",null,"Altitude "+d(o(a).p_a_elevation)+" m",1)])]),t("fieldset",null,[J,t("ul",null,[t("li",null,"Latitude "+d(o(a).la_b),1),t("li",null,"Longitude "+d(o(a).lo_b),1),t("li",null,"Altitude "+d(o(a).p_b_elevation)+" m",1)])])])):$("",!0)],64))}},O={class:"grid"},R={__name:"ViewCalculate",setup(e){return document.title="Calculate points",(a,_)=>(v(),g("div",O,[t("div",null,[j(D)]),t("div",null,[j(K)])]))}};export{R as default};