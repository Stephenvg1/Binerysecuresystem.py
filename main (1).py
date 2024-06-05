import random


def encode_data(data):
    """Encodes data using the pattern '01 10' to represent bits."""
    encoded_data = []
    for bit in data:
        if bit == '0':
            encoded_data.extend(['01', '10'])
        elif bit == '1':
            encoded_data.extend(['10', '01'])
    return encoded_data


def decode_data(encoded_data):
    """Decodes data from the '01 10' pattern."""
    decoded_data = []
    for i in range(0, len(encoded_data), 2):
        if encoded_data[i:i + 2] == ['01', '10']:
            decoded_data.append('0')
        elif encoded_data[i:i + 2] == ['10', '01']:
            decoded_data.append('1')
    return ''.join(decoded_data)


# Example usage
data_to_encode = '10101'
encoded = encode_data(data_to_encode)
print(f"Encoded data: {encoded}")

decoded = decode_data(encoded)
print(f"Decoded data: {decoded}")


class ReversedToken:

    def __init__(self, security, efficiency, reliability, scalability,
                 ease_of_use, data, timestamp, color):
        self.security = security
        self.efficiency = efficiency
        self.reliability = reliability
        self.scalability = scalability
        self.ease_of_use = ease_of_use
        self.data = data
        self.timestamp = timestamp
        self.color = color

    def evaluate(self):
        if self.security < 8 and self.efficiency < 7 and self.reliability < 9 and self.scalability < 8 and self.ease_of_use < 6:
            return "Token and link are highly effective for the energy system."
        else:
            return "Token and link may not be effective for the energy system."

    def get_random_color(self):
        colors = ["red", "blue", "green", "yellow", "orange", "purple"]
        return random.choice(colors)


reversed_token = ReversedToken(5, 6, 8, 7, 5, "Energy Harvesting Data",
                               1643723400, None)
reversed_token.color = reversed_token.get_random_color()
evaluation = reversed_token.evaluate()
print(evaluation)
print("Data:", reversed_token.data)
print("Timestamp:", reversed_token.timestamp)
print("Color:", reversed_token.color)
