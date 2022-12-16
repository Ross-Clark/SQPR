from unittest import TestCase

from src.sqpr import generate_comment, generate_comment_list


class sqpr_test(TestCase):

    issue = {
            'key': 'AYQ-eQkEIpkkQLaIoFS9',
            'rule': 'python:S1542',
            'severity': 'MAJOR',
            'component': 'DCT_Campaigns_Resource_Centre:FrontEndTests/steps/CRCV3_Main_Steps.py', 
            'project': 'DCT_Campaigns_Resource_Centre', 
            'line': 93, 
            'hash': '23af17078acb488072cdba1991d52b98', 
            'textRange': {'startLine': 93, 'endLine': 93, 'startOffset': 4, 'endOffset': 29},
            'flows': [], 
            'status': 'OPEN', 
            'message': 'Rename function "Login_fields_valid_Inputs" to match the regular expression ^[a-z_][a-z0-9_]*$.', 
            'effort': '10min', 
            'debt': '10min', 
            'author': 'prabhu.swamy1@nhs.net', 
            'tags': ['convention'], 
            'creationDate': '2022-11-03T16:26:25+0000', 
            'updateDate': '2022-11-03T17:10:07+0000', 
            'type': 'CODE_SMELL', 
            'pullRequest': '164', 
            'scope': 'MAIN'
        }

    def test_generate_comment(self):
        expected = {
            "path": "FrontEndTests/steps/CRCV3_Main_Steps.py",
            "line": 93,
            "body": "Rename function \"Login_fields_valid_Inputs\" to match the regular expression ^[a-z_][a-z0-9_]*$.",
        }

        actual = generate_comment(self.issue)

        self.assertEqual(expected, actual)

    def test_generate_comment_list(self):

        expected = [{
            "path": "FrontEndTests/steps/CRCV3_Main_Steps.py",
            "line": 93,
            "body": "Rename function \"Login_fields_valid_Inputs\" to match the regular expression ^[a-z_][a-z0-9_]*$.",
        }]

        actual = generate_comment_list([self.issue])

        self.assertEqual(expected, actual)
