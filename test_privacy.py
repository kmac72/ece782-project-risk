
from unittest import TestCase
from unittest.mock import Mock, patch

from mycroft.skills.skill_manager import SkillManager
from mycroft.client.speech.mic import ResponsiveRecognizer


class TestSkillManagerPrivacy(TestCase):

    def setUp(self):

        # Create SkillManager object for testing its functions below
        self.skill_manager = SkillManager(Mock())


    def test_install_priority_blacklisted(self):
        
        # Mock up _load_skill called from load_priority
        load_mock = Mock()
        self.skill_manager._load_skill = load_mock

        # Mock up msm components accessed by load_priority
        skill = Mock()
        skill.name = 'foobar'
        skill.is_local = False

        msm_mock = Mock()
        msm_mock.all_skills = [skill]
        self.skill_manager.msm.list = Mock(return_value=[skill])
        self.skill_manager._msm = msm_mock

        # Set privacy settings accessed by load_priority
        self.skill_manager.config = {
            "skills": {
                "blacklisted_skills": ["foobar"],
                "priority_skills": ["foobar"]
            }
        }
        # Call the function we are testing
        self.skill_manager.load_priority()

        # Ensure privacy settings were implemented correctly
        self.assertFalse(msm_mock.install.called)
        load_mock.assert_not_called()

class TestResponsiveRecognizerPrivacy(TestCase):

    def setUp(self):

        self.recognizer = ResponsiveRecognizer(Mock())


    def test_wakeword_found_opt_in(self):

        create_audio_mock = Mock()
        self.recognizer._create_audio_data = create_audio_mock

        self.recognizer.config['opt_in'] = False
        self.recognizer._handle_wakeword_found(None, Mock())

        create_audio_mock.assert_not_called()
