from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)

# add sample inputs
price, qty = 450.00, 3
total = calculate_total(price, qty)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)

print(f"Total cost: ${total:.2f}")
print(f"Requires review: {review}")
print(f"Approval tier: {tier}")
print(f"10% discount: ${discounted_price:.2f}")
