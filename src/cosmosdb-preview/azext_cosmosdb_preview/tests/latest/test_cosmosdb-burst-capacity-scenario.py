# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))

class Cosmosdb_previewBurstCapacityScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_cosmosdb_sql_burst_capacity', location='australiaeast')
    def test_cosmosdb_burst_capacity(self):
        col = self.create_random_name(prefix='cli', length=15)
        db_name = self.create_random_name(prefix='cli', length=15)
        # Assumption: There exists a cosmosTest rg.
        self.kwargs.update({
            'rg' : 'cosmosTest',
            'acc': 'burst-test',
            'loc': 'australiaeast',
            'tar': '0=1200 1=1200',
            'src': '2'
        })

        #create burst capacity enabled account
        self.cmd('az cosmosdb create -n {acc} -g {rg} --enable-burst-capacity')
        self.cmd('az cosmosdb show -n {acc} -g {rg}', checks=[
            self.check('enableBurstCapacity', True),
        ])
        print('Created burst capacity enabled account')

        #disable burst capacity
        self.cmd('az cosmosdb create -n {acc} -g {rg} --enable-burst-capacity false')
        self.cmd('az cosmosdb show -n {acc} -g {rg}', checks=[
            self.check('enableBurstCapacity', False),
        ])
        print('Disabled burst capacity')

        #enable burst capacity
        self.cmd('az cosmosdb create -n {acc} -g {rg} --enable-burst-capacity')
        self.cmd('az cosmosdb show -n {acc} -g {rg}', checks=[
            self.check('enableBurstCapacity', True),
        ])
        print('Enabled burst capacity')