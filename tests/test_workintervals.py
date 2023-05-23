from pymeistertask.workintervals import Workinterval

from .base import BaseTest


class TestWorkintervalAPI(BaseTest):
    def test_create(self):
        with self.recorder.use_cassette("workintervalapi_create"):
            project, section, task, workinterval = self.create_workinterval()

            assert isinstance(workinterval, Workinterval)
            assert type(workinterval.id) is int

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_get(self):
        with self.recorder.use_cassette("workintervalapi_get"):
            project, section, task, workinterval = self.create_workinterval()
            same_workinterval = self.api.workinterval.get(id=workinterval.id)

            assert isinstance(same_workinterval, Workinterval)
            assert workinterval.id == same_workinterval.id

            self.api.projects.update(id=project.id, data={"status": 4})

    def test_delete(self):
        with self.recorder.use_cassette("workintervalapi_delete"):
            project, section, task, tasklabel = self.create_workinterval()
            deleted = self.api.workinterval.delete(id=tasklabel.id)

            assert deleted is True

            self.api.projects.update(id=project.id, data={"status": 4})


class TestWorkinterval(BaseTest):
    def test_repr(self):
        with self.recorder.use_cassette("workinterval_repr"):
            project, section, task, workinterval = self.create_workinterval()

            assert repr(workinterval) is not None

            self.api.projects.update(id=project.id, data={"status": 4})
