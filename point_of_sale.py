# def scanning_code(code):
#     if code == "12345":
#         return "$7.25"
#     elif code == "23456":
#         return "$12.50"
#     elif code == "99999":
#         return "Not found"
#     elif code == "":
#         return "Error: empty barcode"

# Refactor

# def scanning_code(code):
#     prices = {
#         "12345": 7.25,
#         "23456": 12.50
#     }
#     if code == "":
#         return "Error: empty barcode"
    
#     if code == "total":
#         pass

#     if code in prices:
#         return f"${prices[code]:.2f}"
#     else:
#         return "Not found"


#Refactor
class PointOfSale:
    def __init__(self):
        self.prices = {
            "12345": 7.25,
            "23456": 12.50
        }
        self.scanned_items = []
    
    def scan(self, code):
        if code == "":
            return "Error: empty barcode"
        
        if code == "total":
            if not self.scanned_items:
                return "$0.00"
            total = sum(self.scanned_items)
            return f"${total:.2f}"

        if code in self.prices:
            price = self.prices[code]
            self.scanned_items.append(price)
            return f"${price:.2f}"
        else:
            return "Not found"
    
pos = PointOfSale()

def scanning_code(code):
    return pos.scan(code)