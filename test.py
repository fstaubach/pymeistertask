from typing import cast
from pymeistertask.tasks import Task
from pymeistertask.api import MeisterTaskAPI
from datetime import datetime, timezone, timedelta
# global meisterApi, projects, taskSections, section, label
meisterApi = MeisterTaskAPI(bearer_token="0697206ca2303722b0ed428766d8d0de1fff39a3008a1d14d298a3f3f78232f0")

## HELPERS ##

projects = {'personal':2374836, 'commerzbank':2376656, 'test':6148935}
taskSections = {"in":8632264, "week":8632272, "progress":8632265, "waiting":8642211,"done":8632266}
section = {'month':8632264, 'today':8632265, 'done':8632266, 'week':8632272, 'waiting':8642211, 'backlog':9886995}
taskSectionsCoba = {'in':8639453, 'week':8646374, 'progress':8639454, 'waiting':8646359}
label = {"5min":1918908, "1std":1918909, "3std":1918910, "20min":1918913, "1tag":1918915, "wichtig":1922669, "freizeit":2964859, "unwichtig":3927636}

# meisterApi.projects.all()
# print('Test')

task = meisterApi.tasks.get(101223552)        
    
    

