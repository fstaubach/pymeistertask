from .resource import Resource, ResourceAPI


class Workinterval(Resource):
    _repr_attrs = ("id", "task_id", "person_id")


class WorkintervalsAPI(ResourceAPI):
    _resource = Workinterval

    def create(self, task_id, data):
        return self._create_object(
            url="/tasks/{task_id}/work_intervals".format(task_id=task_id), data=data
        )

    def update(self, id, data):
        return self._update_object(url="/work_intervals/{id}".format(id=id), data=data)

    def delete(self, id):
        return self._delete_object(url="/work_intervals/{id}".format(id=id))

    def filter_by_task(self, task_id, **kwargs):
        return self._get_list(url="/tasks/{task_id}/work_intervals".format(task_id=task_id), **kwargs)

    def filter_by_project(self, project_id, **kwargs):
        return self._get_list(url="/projects/{project_id}/work_intervals".format(task_id=project_id), **kwargs)