from abc import ABC, abstractmethod


class CheckoutState(ABC):

    @abstractmethod
    def add_item(self, item) -> CheckoutState: ...

    @abstractmethod
    def review_cart(self) -> CheckoutState: ...

    @abstractmethod
    def enter_shipping_info(self, info) -> CheckoutState: ...

    @abstractmethod
    def process_payment(self) -> CheckoutState: ...


class EmptyCartState(CheckoutState):

    def add_item(self, item) -> CheckoutState:
        print(f"Item {item} added to cart.")
        return ItemsInCartState()

    def review_cart(self) -> CheckoutState:
        print("Cart is empty. Cannot review.")
        return self

    def enter_shipping_info(self, info) -> CheckoutState:
        print("Cart is empty. Cannot enter shipping info.")
        return self

    def process_payment(self) -> CheckoutState:
        print("Cart is empty. Cannot process payment.")
        return self

class ItemsInCartState(CheckoutState):

    def add_item(self, item) -> CheckoutState:
        print(f"Item {item} added to cart.")
        return self

    def review_cart(self) -> CheckoutState:
        print("Reviewing cart items.")
        return ShippingInfoState()

    def enter_shipping_info(self, info) -> CheckoutState:
        print("Please review cart before entering shipping info.")
        return self

    def process_payment(self) -> CheckoutState:
        print("Please review cart and enter shipping info before processing payment.")
        return self

class ShippingInfoState(CheckoutState):

    def add_item(self, item) -> CheckoutState:
        print("Cannot add items after entering shipping info.")
        return self

    def review_cart(self) -> CheckoutState:
        print("Reviewing cart items again.")
        return self

    def enter_shipping_info(self, info) -> CheckoutState:
        print(f"Shipping info {info} entered.")
        return PaymentProcessingState()

    def process_payment(self) -> CheckoutState:
        print("Please enter shipping info before processing payment.")
        return self

class PaymentProcessingState(CheckoutState):

    def add_item(self, item) -> CheckoutState:
        print("Cannot add items during payment processing.")
        return self

    def review_cart(self) -> CheckoutState:
        print("Cannot review cart during payment processing.")
        return self

    def enter_shipping_info(self, info) -> CheckoutState:
        print("Cannot enter shipping info during payment processing.")
        return self

    def process_payment(self) -> CheckoutState:
        print("Payment processed successfully. Order complete!")
        return EmptyCartState()


class CheckoutContext:

    def __init__(self) -> None:
        self.state: CheckoutState = EmptyCartState()

    def add_item(self, item) -> None:
        self.state = self.state.add_item(item)

    def review_cart(self) -> None:
        self.state = self.state.review_cart()

    def enter_shipping_info(self, info) -> None:
        self.state = self.state.enter_shipping_info(info)

    def process_payment(self) -> None:
        self.state = self.state.process_payment()


if __name__ == "__main__":
    checkout = CheckoutContext()
    checkout.add_item("Laptop")
    checkout.review_cart()
    checkout.enter_shipping_info("123 Main St, Anytown, USA")
    checkout.process_payment()

    # Trying to add item after review / shipping
    checkout.add_item("Mouse")
    checkout.review_cart()
    checkout.add_item("Monitor")
    checkout.enter_shipping_info("456 Elm St, Othertown, USA")
    checkout.review_cart()
    checkout.process_payment()