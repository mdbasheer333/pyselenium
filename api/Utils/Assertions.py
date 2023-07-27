class CustomAssertion:

    def compare_values(self, exp_dct, act_dct):
        for key in exp_dct:
            assert exp_dct[key] == act_dct[key], f'mistamch exp is {exp_dct[key]} and act is {act_dct[key]}'
            print(f'correct exp is {exp_dct[key]} and act is {act_dct[key]}')

    def soft_compare_values(self, exp_dct, act_dct):
        failcount = 0
        for key in exp_dct:
            try:
                if exp_dct[key] != act_dct[key]:
                    failcount = failcount + 1
                    print(f'incorrect correct exp is {exp_dct[key]} and act is {act_dct[key]}')
                else:
                    print(f'correct exp is {exp_dct[key]} and act is {act_dct[key]}')
            except:
                failcount = failcount + 1
                print(f' some issue with key {key}')
        assert failcount == 0, f'some thing is mismatch'
