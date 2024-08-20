
from product import Product
from coupon import Coupon

def initialize_products():
    return [
        Product("H-E-B Two Bite Brownies", 85294241, False, True, 3.61),
        Product("Halo Top Vanilla Bean Ice Cream", 95422042, False, False, 3.31),
        Product("H-E-B Select Ingredients Creamy Creations Vanilla Bean Ice Cream", 64267055, True, True, 9.83),
        Product("Aveeno Daily Moisturizing Body Wash", 12821859, True, False, 5.11),
        Product("Hershey's Chocolate Syrup", 23991994, False, False, 9.47),
        Product("GoGo squeeZ Applesauce Pouches", 30224576, False, False, 7.58),
        Product("H-E-B Organics Unbleached All Purpose Flour", 50338388, True, True, 5.89),
        Product("Heritage Ranch by H-E-B Baked Pumpkin Dog Treats", 31001002, True, True, 5.11),
        Product("KODI Red Matte Stainless Steel Low Ball Tumbler", 87467463, False, True, 1.5),
        Product("H-E-B Artisan Yellow Cheddar Cheese", 40514710, True, True, 11.48),
        Product("H-E-B Sugar Rush Dream Melon", 56037921, True, True, 8.4),
        Product("H-E-B Chocolate Milk", 49057828, True, True, 6.42),
        Product("Oroweat Extra Crisp Fork-Split English Muffins", 92374672, True, False, 2.83),
        Product("H-E-B Organics Frozen Berry Blend", 73354627, True, True, 4.77),
        Product("H-E-B Select Ingredients Unsweetened Coconut Sparkling Water 12 oz Cans", 65290137, True, True, 14.18),
        Product("H-E-B Spaghetti", 30532705, False, True, 4.86),
        Product("H-E-B Prime 1 Beef Brisket Steak Burgers, 2 ct", 29846569, True, True, 8.65),
        Product("Tofurky", 61411728, True, False, 8.15),
        Product("H-E-B Select Ingredients Chocolate Hummus", 58267213, True, True, 9.29),
        Product("Heinz Tomato Ketchup", 73018836, False, False, 12.8),
        Product("H-E-B Queso Classic, Mild", 12338101, False, True, 12.41),
        Product("Central Market Mild Peach Salsa", 99828459, False, True, 1.16),
        Product("H-E-B Natural Ground Bison", 14064431, False, True, 12.52),
        Product("H-E-B Texas Style Unsweet Tea", 77915014, True, True, 7.04),
        Product("H-E-B Original Bacon", 48067887, False, True, 7.15),
        Product("H-E-B Cotton Swabs with Paper Sticks", 48426066, False, True, 9.72),
        Product("Central Market Organics Mushroom Pasta Sauce", 64474859, True, True, 7.12),
        Product("H-E-B Vegetable Medley", 11407191, True, True, 4.81),
        Product("Beyond Meat Beyond Beef Plant Based Ground", 99657156, False, False, 3.81),
        Product("H-E-B Wild Caught Sockeye Salmon Fillet", 75821377, True, True, 12.43)
    ]

def initialize_coupons():
    return [
        Coupon("Brownie Discount", 85294241, 0.79),
        Coupon("Tofurky Discount", 61411728, 1.01),
        Coupon("Spaghetti Discount", 30532705, 1.83)
    ]

def calculate_subtotal(products):
    return sum(product.price for product in products)

def calculate_tax_total(products):
    tax_rate = 0.0825
    return sum(product.price * tax_rate for product in products if product.is_taxable)

def apply_coupons(products, coupons):
    for coupon in coupons:
        for product in products:
            if product.sku == coupon.applied_sku:
                product.price = max(0, product.price - coupon.discount_price)

def print_totals(subtotal, tax_total, grand_total):
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax Total: ${tax_total:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")

if __name__ == "__main__":
    products = initialize_products()
    coupons = initialize_coupons()

    # Calculate totals without applying coupons
    subtotal = calculate_subtotal(products)
    tax_total = calculate_tax_total(products)
    grand_total = subtotal + tax_total

    print("
--- Totals Without Coupons ---")
    print_totals(subtotal, tax_total, grand_total)

    # Apply coupons and recalculate totals
    apply_coupons(products, coupons)
    subtotal = calculate_subtotal(products)
    tax_total = calculate_tax_total(products)
    grand_total = subtotal + tax_total

    print("
--- Totals With Coupons Applied ---")
    print_totals(subtotal, tax_total, grand_total)
