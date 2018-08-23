from flask import Flask, request
import json
from sqlalchemy import create_engine
from fetch import StationDivison, Department

def sel1(request):
    station_name = str(request.args.get('station'))
    department_name = str(request.args.get('department'))
    
    engine = create_engine('sqlite:///app.db')
    con = engine.connect()
    
    s = StationDivison.query.filter_by(station == 'station_name')
    
    d = Department.query.filter_by(division = 's.division')
    cl = Department.query.filter_by(clean = 's.division'+'-'+'department_name')
    st= Department.query.filter_by(staff = 's.division'+'s.division'+'-'+'department_name')
    ir_s = Department.query.filter_by(irctc_s = 's.division'+'-'+'department_name')
    ir_c = Department.query.filter_by(irctc_care = 's.division'+'-'+'department_name')
    bo = Department.query.filter_by(booking = 's.division'+'-'+'department_name')
    me = Department.query.filter_by(medical ='s.division'+'-'+'department_name')
    la= Department.query.filter_by(late = 's.division'+'-'+'department_name')
    wa = Department.query.filter_by(water = 's.division'+'-'+'department_name')
    se= Department.query.filter_by(security == 's.division'+'-'+'department_name')
    el = Department.query.filter_by(electric == 's.division'+'-'+'department_name')
    no = Department.query.filter_by(none == 's.division'+'-'+'department_name')
    
    con.close()
    
    if cl != NULL:
        return Response(json.dumps({'gm':cl.gm,'drm':cl.drm,'clean':cl.clean}), content_type = "json/application")
    if st != NULL:
        return Response(json.dumps({'gm':st.gm,'drm':st.drm,'staff':st.staff}), content_type = "json/application")
    if ir_s != NULL:
        return Response(json.dumps({'gm':ir_s.gm,'drm':ir_s.drm,'irctc_staff':ir_s.irctc_staff}), content_type = "json/application")
    if ir_c != NULL:
        return Response(json.dumps({'gm':ir_c.gm,'drm':ir_c.drm,'irctc_care':ir_c.irctc_care}), content_type = "json/application")
    if bo != NULL:
        return Response(json.dumps({'gm':bo.gm,'drm':bo.drm,'booking':bo.booking}), content_type = "json/application")
    if me != NULL:
        return Response(json.dumps({'gm':me.gm,'drm':me.drm,'medical':me.medical}), content_type = "json/application")
    if la != NULL:
        return Response(json.dumps({'gm':la.gm,'drm':la.drm,'late':la.late}), content_type = "json/application")
    if wa != NULL:
        return Response(json.dumps({'gm':wa.gm,'drm':wa.drm,'water':wa.water}), content_type = "json/application")
    if se != NULL:
        return Response(json.dumps({'gm':se.gm,'drm':se.drm,'security':se.security}), content_type = "json/application")
    if el != NULL:
        return Response(json.dumps({'gm':el.gm,'drm':el.drm,'electric':el.electric}), content_type = "json/application")
    if no != NULL:
        return Response(json.dumps({'gm':no.gm,'drm':no.drm,'none':no.none}), content_type = "json/application")
        
