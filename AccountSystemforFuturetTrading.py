import pandas as pd

class AccountingSystemforFutureTrading:
    def __init__(self):
        self.FrozenFunds = {}
        self.LiquidFunds = {}
        self.Margin_Long = {}
        self.Margin_Short = {}
        self.IdleFunds = {}
        self.Position_Long = {}
        self.Position_Short = {}
        self.Position_Spread = {}
        self.new_row = {}
    def create_account(self, account_type, account_name):
        if account_type == 'FrozenFunds':
            self.FrozenFunds[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'LiquidFunds':
            self.LiquidFunds[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'Margin_Long':
            self.Margin_Long[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'Margin_Short':
            self.Margin_Short[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'IdleFunds':
            self.IdleFunds[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'Position_Long':
            self.Position_Long[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'Position_Short':
            self.Position_Short[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})


    def debit(self, account_type, account_name, amount,date,notes=None):

        if account_type == 'FrozenFunds':
            a = len(self.FrozenFunds[account_name])
            if a != 0:
                last_balence = self.FrozenFunds[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':amount+last_balence,'Notes':notes}
            self.FrozenFunds[account_name]=self.FrozenFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'LiquidFunds':
            a = len(self.LiquidFunds[account_name])
            if a != 0:
                last_balence = self.LiquidFunds[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':amount+last_balence,'Notes':notes}
            self.LiquidFunds[account_name]=self.LiquidFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Margin_Long':
            a = len(self.Margin_Long[account_name])
            if a != 0:
                last_balence = self.Margin_Long[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':-amount+last_balence,'Notes':notes}
            self.Margin_Long[account_name]=self.Margin_Long[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Margin_Short':
            a = len(self.Margin_Short[account_name])
            if a != 0:
                last_balence = self.Margin_Short[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':-amount+last_balence,'Notes':notes}
            self.Margin_Short[account_name]=self.Margin_Short[account_name].append(self.new_row, ignore_index=True)

        elif account_type == 'IdleFunds':
            a = len(self.IdleFunds[account_name])
            if a != 0:
                last_balence = self.IdleFunds[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':-amount+last_balence,'Notes':notes}
            self.IdleFunds[account_name]=self.IdleFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Position_Long':
            a = len(self.Position_Long[account_name])
            if a != 0:
                last_balence = self.Position_Long[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':-amount+last_balence,'Notes':notes}
            self.Position_Long[account_name]=self.Position_Long[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Position_Short':
            a = len(self.Position_Short[account_name])
            if a != 0:
                last_balence = self.Position_Short[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':-amount+last_balence,'Notes':notes}
            self.Position_Short[account_name]=self.Position_Short[account_name].append(self.new_row, ignore_index=True)
        
    
    def credit(self, account_type, account_name, amount,date,notes=None):
        if account_type == 'FrozenFunds':
            a = len(self.FrozenFunds[account_name])
            if a != 0:
                last_balence = self.FrozenFunds[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':-amount+last_balence,'Notes':notes}
            self.FrozenFunds[account_name]=self.FrozenFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'LiquidFunds':
            a = len(self.LiquidFunds[account_name])
            if a != 0:
                last_balence = self.LiquidFunds[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':-amount+last_balence,'Notes':notes}
            self.LiquidFunds[account_name]=self.LiquidFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Margin_Long':
            a = len(self.Margin_Long[account_name])
            if a != 0:
                last_balence = self.Margin_Long[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':amount+last_balence,'Notes':notes}
            self.Margin_Long[account_name]=self.Margin_Long[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Margin_Short':
            a = len(self.Margin_Short[account_name])
            if a != 0:
                last_balence = self.Margin_Short[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':amount+last_balence,'Notes':notes}
            self.Margin_Short[account_name]=self.Margin_Short[account_name].append(self.new_row, ignore_index=True)

        elif account_type == 'IdleFunds':
            a = len(self.IdleFunds[account_name])
            if a != 0:
                last_balence = self.IdleFunds[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':amount+last_balence,'Notes':notes}
            self.IdleFunds[account_name]=self.IdleFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Position_Long':
            a = len(self.Position_Long[account_name])
            if a != 0:
                last_balence = self.Position_Long[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':amount+last_balence,'Notes':notes}
            self.Position_Long[account_name]=self.Position_Long[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Position_Short':
            a = len(self.Position_Short[account_name])
            if a != 0:
                last_balence = self.Position_Short[account_name].loc[a-1,'Balence']  
            else:
                last_balence = 0
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':amount+last_balence,'Notes':notes}
            self.Position_Short[account_name]=self.Position_Short[account_name].append(self.new_row, ignore_index=True)


    def get_balance(self, account_type, account_name):
        if account_type == 'FrozenFunds':
            return self.FrozenFunds[account_name].loc[0:,'Balence'].sum()
        elif account_type == 'LiquidFunds':
            return self.LiquidFunds[account_name].loc[0:,'Balence'].sum()
        elif account_type == 'Margin':
            return self.Margin[account_name].loc[0:,'Balence'].sum()
        elif account_type == 'IdleFunds':
            return self.IdleFunds[account_name].loc[0:,'Balence'].sum()

# accountkeeper=AccountingSystemforFutureTrading()
# accountkeeper.create_account('FrozenFunds','frozenforfuture')
# accountkeeper.create_account('Margin','margin')
# accountkeeper.debit('FrozenFunds','frozenforfuture',100,'2020-07-06')
# accountkeeper.credit('Margin','margin',100,'2020-07-06')
# print('frozenforfuture',accountkeeper.FrozenFunds['frozenforfuture'])
# print('margin_1',accountkeeper.Margin['margin'])
# print(accountkeeper.get_balance('FrozenFunds','frozenforfuture'))