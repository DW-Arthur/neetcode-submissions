class StockSpanner:

    def __init__(self):
        # Monotonic decreasing stack storing pairs: [price, span]
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Accumulate the spans of all consecutive past days with price <= current price
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append([price, span])
        return span