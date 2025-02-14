@dataclass(frozen=True)
class Transaction:
    amount: float
    when: datetime = field(default_factory=datetime.now)


@dataclass
class History:
    transactions: list[Transaction] = field(default_factory=list)

    def push(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def pop(self) -> Transaction:
        return self.transactions.pop()


@dataclass
class Account:
    balance: float = 0.0
    history: History = field(default_factory=History)

    def deposit(self, amount: float) -> None:
        transaction = Transaction(amount)
        self.balance += transaction.amount
        self.history.push(transaction)

    def undo(self):
        transaction = self.history.pop()
        self.balance -= transaction.amount