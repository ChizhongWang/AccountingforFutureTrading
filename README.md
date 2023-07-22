# AccountingforFutureTrading
用于期货交易的会计账簿系统



# 期货交易账户的会计恒等式

## 字符说明：

$Asset:总资产，净值。也称为“客户总权益”$\
$Frozen\quad Funds:冻结资金$\
$Liquid\quad Funds:流动资金$\
$Margin:保证金$\
$capital\quad gains:资本利得，通过多头低买高卖和空头高卖低买获得$ \
$Idle\quad Funds:闲置资金$\
$Interest\quad Revenue:闲置资金产生的活期存款水平的利息$\
$margin_i:第i笔开仓冻结的保证金$\
$margin_{i^*}:目前持仓中开仓时间最早的保证金$\
$margin_{i^{**}}:目前持仓中开仓时间最晚的保证金$\
$Capital\quad Gains\quad From\quad Long:多头方向的资本利得$\
$Capital\quad Gains\quad From\quad Short:空头方向的资本利得$\
$value_{i,0}:第i笔开仓所锚定的合约在时刻0的价值$\
$capital\quad gains\quad from\quad long_{i,\tau}:第i笔开仓，如果是多头方向，在时刻\tau 的资本利得$\
$capital\quad gains\quad from\quad short_{i,\tau}:第i笔开仓，如果是空头方向，在时刻\tau 的资本利得$

## 会计恒等式 &nbsp; Accounting&nbsp;Equation&nbsp;in&nbsp;Future&nbsp;Trading

$$Frozen\quad Funds+Liquid\quad Funds = Margin+Idle\quad Funds \tag{1}$$

$$Asset = Frozen\quad Funds+Liquid\quad Funds \tag{2}$$

$$Margin = \Sigma_{i=i^{*}}^{i^{**}}margin_i\tag{3}$$

$$capital\quad gains\quad from\quad long_{i,\tau} = value_{i,\tau} -value_{i,0}\tag{4}$$

$$capital\quad gains\quad from\quad short_{i,\tau} = -(value_{i,\tau} -value_{i,0}\tag{5})$$

$$Idle\quad Fund_i = Idle\quad Fund_{i-1}*(1+0.007/365)+Capital\quad Gains_i\tag{6}$$

### 四大科目下都有哪些账户？&nbsp; Which&nbsp; Accounts&nbsp; Fall&nbsp; under&nbsp; the &nbsp;Four&nbsp; Major&nbsp; Categories?
$frozen\quad for\quad future\in Frozen\quad Funds$\
$cash\in Liquid\quad Funds$\
$margin_i \in Margin$\
$capital\quad gains\in Idle\quad Funds$


## 沿用复式记账的规则&nbsp;Double-Entry Accounting
1.会计恒等式左边的科目增加记为借Debit，减少记为贷Credit；右边的科目增加记为贷Credit，减少记为借Debit。
2.有借必有贷，借贷必相等。

Python代码实现示例：
```python
import pandas as pd

class AccountingSystemforFutureTrading:
    def __init__(self):
        self.FrozenFunds = {}
        self.LiquidFunds = {}
        self.Margin = {}
        self.IdleFunds = {}
        self.new_row = {}
    def create_account(self, account_type, account_name):
        if account_type == 'FrozenFunds':
            self.FrozenFunds[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'LiquidFunds':
            self.LiquidFunds[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'Margin':
            self.Margin[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})
        elif account_type == 'IdleFunds':
            self.IdleFunds[account_name] = pd.DataFrame({'Date':[],'Debit':[],'Credit':[],'Balence':[],'Notes':[]})

    def debit(self, account_type, account_name, amount,date,notes=None):
        if account_type == 'FrozenFunds':
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':amount,'Notes':notes}
            self.FrozenFunds[account_name]=self.FrozenFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'LiquidFunds':
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':amount,'Notes':notes}
            self.LiquidFunds[account_name]=self.LiquidFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Margin':
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':-amount,'Notes':notes}
            self.Margin[account_name]=self.Margin[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'IdleFunds':
            self.new_row = {'Date':date,'Debit':amount,'Credit':0,'Balence':-amount,'Notes':notes}
            self.IdleFunds[account_name]=self.IdleFunds[account_name].append(self.new_row, ignore_index=True)

    def credit(self, account_type, account_name, amount,date,notes=None):
        if account_type == 'FrozenFunds':
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':-amount,'Notes':notes}
            self.FrozenFunds[account_name]=self.FrozenFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'LiquidFunds':
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':-amount,'Notes':notes}
            self.LiquidFunds[account_name]=self.LiquidFunds[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'Margin':
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':amount,'Notes':notes}
            self.Margin[account_name]=self.Margin[account_name].append(self.new_row, ignore_index=True)
        elif account_type == 'IdleFunds':
            self.new_row = {'Date':date,'Debit':0,'Credit':amount,'Balence':amount,'Notes':notes}
            self.IdleFunds[account_name]=self.IdleFunds[account_name].append(self.new_row, ignore_index=True)

    def get_balance(self, account_type, account_name):
        if account_type == 'FrozenFunds':
            return self.FrozenFunds[account_name].loc[0:,'Balence'].sum()
        elif account_type == 'LiquidFunds':
            return self.LiquidFunds[account_name].loc[0:,'Balence'].sum()
        elif account_type == 'Margin':
            return self.Margin[account_name].loc[0:,'Balence'].sum()
        elif account_type == 'IdleFunds':
            return self.IdleFunds[account_name].loc[0:,'Balence'].sum()

```
## 开始添加交易！
### 初始化账户
```python
accountkeeper = AccountingSystemforFutureTrading()
accountkeeper.create_account(FrozenFunds,frozenforfuture)
accountkeeper.create_account(LiquidFunds,cash)
accountkeeper.create_account(IdleFunds,idlefunds)
# 初始化账户，给现金账户注资
accountkeeper.debit(LiquidFunds,cash,100)
accountkeeper.credit(IdleFunds,idlefunds,100)
```
### 第一次开仓
```python
accountkeeper.creat_account(Margin,margin_1)
accountkeeper.debit(FrozenFunds,frozenforfuture,0.005*2*200*102/100)#保证金率*手数*一张合约的面值*合约价格/100
accountkeeper.credit(Margin,margin_1,0.005*2*200*102/100)

```
### 资本利得计账示例
**金额增加记贷方Credit，金额减少记借方Debit**\\
**对于多头，$capital\quad gains\quad from\quad long_{i,\tau} = value_{i,\tau} -value_{i,0}$**\\
**对于空头，$capital\quad gains\quad from\quad short_{i,\tau} = -(value_{i,\tau} -value_{i,0})$**\\
**Balence[k]=sum(Credit[0:k+1])-sum(Debit[0:k+1])**
#### Position_Long_1
| Date | Debit | Credit | Balence | Notes |
| ------ | ------ | ------ | ------ | ------ |
| 2020-07-05 | 0 |  value_{i,1}-value_{i,0}| sum(Credit)-sum(Debit) |开仓后第一个交易日收益为正 |
| 2020-07-05 | Balence[0] |  0| 0 | 每个仓位每日结算后余额应该是0 |

#### cash
| Date | Debit | Credit | Balence | Notes |
| ------ | ------ | ------ | ------ | ------ |
| 2020-07-05 | Position_Long_1.loc[0,'Credit']|  Position_Long_1.loc[0,'Debit']| sum(Debit)-sum(Credit) |借记Cash，如果赚钱的话 |
#### idlefunds
| Date | Debit | Credit | Balence | Notes |
| ------ | ------ | ------ | ------ | ------ |
| 2020-07-05 | Position_Long_1.loc[1,'Credit']|  Position_Long_1.loc[1,'Debit']| sum(Credit)-sum(Debit) |idlefunds对于每一个仓位每日结算后多退少补 |
### 闲置资金账户示例
#### idlefunds
| Date | Debit | Credit | Balence | Notes |
| ------ | ------ | ------ | ------ | ------ |
| 2020-07-05 | 0|  initial cash | sum(Credit)-sum(Debit) |首日接收注资 |
| 2020-07-05 | Position_Long_1.loc[1,'Credit']|  Position_Long_1.loc[1,'Debit']| sum(Credit)-sum(Debit) |idlefunds对于每一个仓位每日结算后多退少补 |
