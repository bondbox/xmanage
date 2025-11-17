# coding:utf-8

import unittest
from unittest import mock

from xmanage.systemd import service
from xmanage.systemd import unit


class TestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service_unit = """[Unit]
Description = Test
After = network.target

[Service]
ExecStart = /usr/local/bin/test -w
Restart = on-abort
RemainAfterExit = yes

[Install]
WantedBy = multi-user.target"""

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sd_path(self):
        self.assertIsInstance(dir(service.sd_path), list)
        self.assertIsInstance(service.sd_path.systemd_system_conf_dir, str)
        self.assertIsInstance(service.sd_path.systemd_system_unit_dirs, tuple)
        self.assertIsInstance(service.sd_path.systemd_system_generator_dirs, tuple)  # noqa:E501

    def test_sd_service_unit_path(self):
        self.assertIsInstance(service.allowed_dirs, tuple)
        self.assertEqual(service.allowed_dirs, service.sd_path.systemd_system_dirs)  # noqa:E501
        self.assertIsInstance(service.sd_service.service_unit_path("test"), str)  # noqa:E501

    @mock.patch.object(service.os.path, "exists")
    @mock.patch.object(service, "open", mock.mock_open())
    @mock.patch.object(service.os, "system", mock.MagicMock())
    def test_sd_service_create_unit(self, mock_exists):
        mock_exists.side_effect = [False, True]
        object = service.sd_service.from_string("")
        self.assertIsInstance(object.create_unit("test"), str)
        self.assertRaises(FileExistsError, object.create_unit, "test")

    @mock.patch.object(service.os.path, "isfile")
    @mock.patch.object(service.os.path, "exists")
    @mock.patch.object(service.os, "remove", mock.MagicMock())
    @mock.patch.object(service.os, "system", mock.MagicMock())
    def test_sd_service_delete_unit(self, mock_exists, mock_isfile):
        mock_isfile.side_effect = [True]
        mock_exists.side_effect = [True]
        self.assertFalse(service.sd_service.delete_unit("test"))

    @mock.patch.object(service, "open")
    @mock.patch.object(service.os.path, "isfile")
    @mock.patch.object(service.os.path, "exists")
    def test_sd_service(self, mock_exists, mock_isfile, mock_open):
        mock_exists.side_effect = [True, True]
        mock_isfile.side_effect = [True, True]
        with mock.mock_open(mock_open, read_data=""):
            object = service.sd_service.from_unit("test.service")
            self.assertIsInstance(object.parser, service.ConfigParser)
            self.assertIn("Unit", object.sections)
            self.assertIn("Install", object.sections)
            self.assertIn("Service", object.sections)

            for i in unit.sd_uf_sec_unit.options:
                object.unit_section.setdefault(i.value, "unit")
            for k in object.unit_section.keys:
                object.unit_section.setdefault(k, "demo")
            for v in object.unit_section.values:
                self.assertEqual(v, "unit")
            for i in unit.sd_uf_sec_install.options:
                object.install_section.setdefault(i.value, "unit")
            for k in object.install_section.keys:
                object.install_section.setdefault(k, "demo")
            for v in object.install_section.values:
                self.assertEqual(v, "unit")
            for i in service.sd_uf_sec_service.options:
                object.service_section.setdefault(i.value, "unit")
            for k in object.service_section.keys:
                object.service_section.setdefault(k, "demo")
            for v in object.service_section.values:
                self.assertEqual(v, "unit")

            object.unit_section.After = "test"
            object.unit_section.AllowIsolate = "test"
            object.unit_section.After = "test"
            object.unit_section.Before = "test"
            object.unit_section.BindsTo = "test"
            object.unit_section.CollectMode = "test"
            object.unit_section.Conflicts = "test"
            object.unit_section.DefaultDependencies = "test"
            object.unit_section.Description = "test"
            object.unit_section.Documentation = "test"
            object.unit_section.FailureAction = "test"
            object.unit_section.FailureActionExitStatus = "test"
            object.unit_section.IgnoreOnIsolate = "test"
            object.unit_section.JobRunningTimeoutSec = "test"
            object.unit_section.JobTimeoutAction = "test"
            object.unit_section.JobTimeoutRebootArgument = "test"
            object.unit_section.JobTimeoutSec = "test"
            object.unit_section.JoinsNamespaceOf = "test"
            object.unit_section.OnFailure = "test"
            object.unit_section.OnFailureJobMode = "test"
            object.unit_section.OnSuccess = "test"
            object.unit_section.OnSuccessJobMode = "test"
            object.unit_section.PartOf = "test"
            object.unit_section.PropagatesReloadTo = "test"
            object.unit_section.PropagatesStopTo = "test"
            object.unit_section.RebootArgument = "test"
            object.unit_section.RefuseManualStart = "test"
            object.unit_section.RefuseManualStop = "test"
            object.unit_section.ReloadPropagatedFrom = "test"
            object.unit_section.Requires = "test"
            object.unit_section.RequiresMountsFor = "test"
            object.unit_section.Requisite = "test"
            object.unit_section.SourcePath = "test"
            object.unit_section.StartLimitAction = "test"
            object.unit_section.StartLimitBurst = "test"
            object.unit_section.StartLimitIntervalSec = "test"
            object.unit_section.StopPropagatedFrom = "test"
            object.unit_section.StopWhenUnneeded = "test"
            object.unit_section.SuccessAction = "test"
            object.unit_section.SuccessActionExitStatus = "test"
            object.unit_section.SurviveFinalKillSignal = "test"
            object.unit_section.Upholds = "test"
            object.unit_section.Wants = "test"
            for _, v in object.unit_section:
                self.assertEqual(v, "test")

            object.install_section.Alias = "test"
            object.install_section.Also = "test"
            object.install_section.DefaultInstance = "test"
            object.install_section.RequiredBy = "test"
            object.install_section.UpheldBy = "test"
            object.install_section.WantedBy = "test"
            for _, v in object.install_section:
                self.assertEqual(v, "test")

            object.service_section.BusName = "test"
            object.service_section.ExecCondition = "test"
            object.service_section.ExecReload = "test"
            object.service_section.ExecStart = "test"
            object.service_section.ExecStartPost = "test"
            object.service_section.ExecStartPre = "test"
            object.service_section.ExecStop = "test"
            object.service_section.ExecStopPost = "test"
            object.service_section.ExitType = "test"
            object.service_section.FileDescriptorStoreMax = "test"
            object.service_section.FileDescriptorStorePreserve = "test"
            object.service_section.GuessMainPID = "test"
            object.service_section.NonBlocking = "test"
            object.service_section.NotifyAccess = "test"
            object.service_section.OOMPolicy = "test"
            object.service_section.OpenFile = "test"
            object.service_section.PIDFile = "test"
            object.service_section.ReloadSignal = "test"
            object.service_section.RemainAfterExit = "test"
            object.service_section.Restart = "test"
            object.service_section.RestartForceExitStatus = "test"
            object.service_section.RestartMaxDelaySec = "test"
            object.service_section.RestartMode = "test"
            object.service_section.RestartPreventExitStatus = "test"
            object.service_section.RestartSec = "test"
            object.service_section.RestartSteps = "test"
            object.service_section.RuntimeMaxSec = "test"
            object.service_section.RuntimeRandomizedExtraSec = "test"
            object.service_section.RootDirectoryStartOnly = "test"
            object.service_section.Sockets = "test"
            object.service_section.SuccessExitStatus = "test"
            object.service_section.TimeoutAbortSec = "test"
            object.service_section.TimeoutSec = "test"
            object.service_section.TimeoutStartFailureMode = "test"
            object.service_section.TimeoutStartSec = "test"
            object.service_section.TimeoutStopFailureMode = "test"
            object.service_section.TimeoutStopSec = "test"
            object.service_section.Type = "test"
            object.service_section.USBFunctionDescriptors = "test"
            object.service_section.USBFunctionStrings = "test"
            object.service_section.WatchdogSec = "test"
            for _, v in object.service_section:
                self.assertEqual(v, "test")

            self.assertEqual(object.unit_section.name, "Unit")
            self.assertEqual(object.unit_section.After, "test")
            self.assertEqual(object.unit_section.AllowIsolate, "test")
            self.assertEqual(object.unit_section.Before, "test")
            self.assertEqual(object.unit_section.BindsTo, "test")
            self.assertEqual(object.unit_section.CollectMode, "test")
            self.assertEqual(object.unit_section.Conflicts, "test")
            self.assertEqual(object.unit_section.DefaultDependencies, "test")
            self.assertEqual(object.unit_section.Description, "test")
            self.assertEqual(object.unit_section.Documentation, "test")
            self.assertEqual(object.unit_section.FailureAction, "test")
            self.assertEqual(object.unit_section.FailureActionExitStatus, "test")  # noqa:E501
            self.assertEqual(object.unit_section.IgnoreOnIsolate, "test")
            self.assertEqual(object.unit_section.JobRunningTimeoutSec, "test")
            self.assertEqual(object.unit_section.JobTimeoutAction, "test")
            self.assertEqual(object.unit_section.JobTimeoutRebootArgument, "test")  # noqa:E501
            self.assertEqual(object.unit_section.JobTimeoutSec, "test")
            self.assertEqual(object.unit_section.JoinsNamespaceOf, "test")
            self.assertEqual(object.unit_section.OnFailure, "test")
            self.assertEqual(object.unit_section.OnFailureJobMode, "test")
            self.assertEqual(object.unit_section.OnSuccess, "test")
            self.assertEqual(object.unit_section.OnSuccessJobMode, "test")
            self.assertEqual(object.unit_section.PartOf, "test")
            self.assertEqual(object.unit_section.PropagatesReloadTo, "test")
            self.assertEqual(object.unit_section.PropagatesStopTo, "test")
            self.assertEqual(object.unit_section.RebootArgument, "test")
            self.assertEqual(object.unit_section.RefuseManualStart, "test")
            self.assertEqual(object.unit_section.RefuseManualStop, "test")
            self.assertEqual(object.unit_section.ReloadPropagatedFrom, "test")
            self.assertEqual(object.unit_section.Requires, "test")
            self.assertEqual(object.unit_section.RequiresMountsFor, "test")
            self.assertEqual(object.unit_section.Requisite, "test")
            self.assertEqual(object.unit_section.SourcePath, "test")
            self.assertEqual(object.unit_section.StartLimitAction, "test")
            self.assertEqual(object.unit_section.StartLimitBurst, "test")
            self.assertEqual(object.unit_section.StartLimitIntervalSec, "test")
            self.assertEqual(object.unit_section.StopPropagatedFrom, "test")
            self.assertEqual(object.unit_section.StopWhenUnneeded, "test")
            self.assertEqual(object.unit_section.SuccessAction, "test")
            self.assertEqual(object.unit_section.SuccessActionExitStatus, "test")  # noqa:E501
            self.assertEqual(object.unit_section.SurviveFinalKillSignal, "test")  # noqa:E501
            self.assertEqual(object.unit_section.Upholds, "test")
            self.assertEqual(object.unit_section.Wants, "test")

            self.assertEqual(object.install_section.name, "Install")
            self.assertEqual(object.install_section.Alias, "test")
            self.assertEqual(object.install_section.Also, "test")
            self.assertEqual(object.install_section.DefaultInstance, "test")
            self.assertEqual(object.install_section.RequiredBy, "test")
            self.assertEqual(object.install_section.UpheldBy, "test")
            self.assertEqual(object.install_section.WantedBy, "test")

            self.assertEqual(object.service_section.name, "Service")
            self.assertEqual(object.service_section.BusName, "test")
            self.assertEqual(object.service_section.ExecCondition, "test")
            self.assertEqual(object.service_section.ExecReload, "test")
            self.assertEqual(object.service_section.ExecStart, "test")
            self.assertEqual(object.service_section.ExecStartPost, "test")
            self.assertEqual(object.service_section.ExecStartPre, "test")
            self.assertEqual(object.service_section.ExecStop, "test")
            self.assertEqual(object.service_section.ExecStopPost, "test")
            self.assertEqual(object.service_section.ExitType, "test")
            self.assertEqual(object.service_section.FileDescriptorStoreMax, "test")  # noqa:E501
            self.assertEqual(object.service_section.FileDescriptorStorePreserve, "test")  # noqa:E501
            self.assertEqual(object.service_section.GuessMainPID, "test")
            self.assertEqual(object.service_section.NonBlocking, "test")
            self.assertEqual(object.service_section.NotifyAccess, "test")
            self.assertEqual(object.service_section.OOMPolicy, "test")
            self.assertEqual(object.service_section.OpenFile, "test")
            self.assertEqual(object.service_section.PIDFile, "test")
            self.assertEqual(object.service_section.ReloadSignal, "test")
            self.assertEqual(object.service_section.RemainAfterExit, "test")
            self.assertEqual(object.service_section.Restart, "test")
            self.assertEqual(object.service_section.RestartForceExitStatus, "test")  # noqa:E501
            self.assertEqual(object.service_section.RestartMaxDelaySec, "test")
            self.assertEqual(object.service_section.RestartMode, "test")
            self.assertEqual(object.service_section.RestartPreventExitStatus, "test")  # noqa:E501
            self.assertEqual(object.service_section.RestartSec, "test")
            self.assertEqual(object.service_section.RestartSteps, "test")
            self.assertEqual(object.service_section.RuntimeMaxSec, "test")
            self.assertEqual(object.service_section.RuntimeRandomizedExtraSec, "test")  # noqa:E501
            self.assertEqual(object.service_section.RootDirectoryStartOnly, "test")  # noqa:E501
            self.assertEqual(object.service_section.Sockets, "test")
            self.assertEqual(object.service_section.SuccessExitStatus, "test")
            self.assertEqual(object.service_section.TimeoutAbortSec, "test")
            self.assertEqual(object.service_section.TimeoutSec, "test")
            self.assertEqual(object.service_section.TimeoutStartFailureMode, "test")  # noqa:E501
            self.assertEqual(object.service_section.TimeoutStartSec, "test")
            self.assertEqual(object.service_section.TimeoutStopFailureMode, "test")  # noqa:E501
            self.assertEqual(object.service_section.TimeoutStopSec, "test")
            self.assertEqual(object.service_section.Type, "test")
            self.assertEqual(object.service_section.USBFunctionDescriptors, "test")  # noqa:E501
            self.assertEqual(object.service_section.USBFunctionStrings, "test")
            self.assertEqual(object.service_section.WatchdogSec, "test")

    @mock.patch.object(service.os.path, "isfile")
    @mock.patch.object(service.os.path, "exists")
    def test_sd_service_not_found(self, mock_exists, mock_isfile):
        mock_exists.return_value = False
        mock_isfile.return_value = False
        self.assertRaises(FileNotFoundError, service.sd_service.from_unit, "test.service")  # noqa:E501


if __name__ == "__main__":
    unittest.main()
