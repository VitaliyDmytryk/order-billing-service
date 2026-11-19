class CustomerProfile:
    def __init__(self, user_id: int, email: str, password_hash: str, city: str, loyalty_points: int):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points


# Ліквідація Stamp Coupling: функція приймає лише примітивні параметри (Data Coupling)
def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    base_rate = 50.0 if city == "Ivano-Frankivsk" else 110.0
    return base_rate + (weight_kg * 12.0)


# Ліквідація Common та Control Coupling: явний параметр tax_rate і виділена функція для стандартного рахунку
def process_standard_invoice(
    amount: float,
    city: str,
    weight_kg: float,
    tax_rate: float = 0.20,
) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


# Окрема функція для звільнених від податку рахунків без побічних ефектів
def process_tax_exempt_invoice(
    amount: float,
    city: str,
    weight_kg: float,
) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
