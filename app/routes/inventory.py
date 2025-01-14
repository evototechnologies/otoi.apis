from flask import Flask, request, jsonify
from app.extensions import db
from app.models import ItemType, ItemCategory, MeasuringUnit, Item, ItemImage
from app.utils.stamping import set_created_fields, set_updated_fields, set_business

app = Flask(__name__)

# ---- ITEM TYPE ENDPOINTS ----
@app.route('/item-types', methods=['GET'])
def get_item_types():
    item_types = ItemType.query.all()
    return jsonify([{'id': it.id, 'name': it.name} for it in item_types])


@app.route('/item-types', methods=['POST'])
def create_item_type():
    data = request.json
    item_type = ItemType(name=data['name'])
    set_created_fields(item_type)  # Set created_by and created_at
    set_business(item_type)  # Set business_id
    db.session.add(item_type)
    db.session.commit()
    return jsonify({'message': 'Item type created successfully'}), 201


@app.route('/item-types/<int:id>', methods=['PUT'])
def update_item_type(id):
    data = request.json
    item_type = ItemType.query.get_or_404(id)
    item_type.name = data['name'] 
    set_updated_fields(item_type)  # Set updated_by and updated_at

    db.session.commit()
    return jsonify({'message': 'Item type updated successfully'})


@app.route('/item-types/<int:id>', methods=['DELETE'])
def delete_item_type(id):
    item_type = ItemType.query.get_or_404(id)
    db.session.delete(item_type)
    db.session.commit()
    return jsonify({'message': 'Item type deleted successfully'})

# ---- ITEM CATEGORY ENDPOINTS ----
@app.route('/item-categories', methods=['GET'])
def get_item_categories():
    categories = ItemCategory.query.all()
    return jsonify([{
        'id': cat.id, 
        'name': cat.name,
        'created_by': cat.created_by,
        'updated_by': cat.updated_by,
        'created_at': cat.created_at,
        'updated_at': cat.updated_at,
        } for cat in categories])


@app.route('/item-categories', methods=['POST'])
def create_item_category():
    data = request.json
    category = ItemCategory(name=data['name'])
    set_created_fields(category)  # Set created_by and created_at
    set_business(category)  # Set business_id
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Item category created successfully'}), 201


@app.route('/item-categories/<int:id>', methods=['PUT'])
def update_item_category(id):
    data = request.json
    category = ItemCategory.query.get_or_404(id)
    category.name = data['name']
    set_updated_fields(category)  # Set updated_by and updated_at
    
    db.session.commit()
    return jsonify({'message': 'Item category updated successfully'})


@app.route('/item-categories/<int:id>', methods=['DELETE'])
def delete_item_category(id):
    category = ItemCategory.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Item category deleted successfully'})

# ---- MEASURING UNIT ENDPOINTS ----
@app.route('/measuring-units', methods=['GET'])
def get_measuring_units():
    units = MeasuringUnit.query.all()
    return jsonify([{
        'id': unit.id, 
        'name': unit.name,
        'created_by': unit.created_by,
        'updated_by': unit.updated_by,
        'created_at': unit.created_at,
        'updated_at': unit.updated_at,
    } for unit in units])


@app.route('/measuring-units', methods=['POST'])
def create_measuring_unit():
    data = request.json
    unit = MeasuringUnit(name=data['name'])
    set_created_fields(unit)  # Set created_by and created_at
    db.session.add(unit)
    db.session.commit()
    return jsonify({'message': 'Measuring unit created successfully'}), 201


@app.route('/measuring-units/<int:id>', methods=['PUT'])
def update_measuring_unit(id):
    data = request.json
    unit = MeasuringUnit.query.get_or_404(id)
    unit.name = data['name']
    set_updated_fields(unit)  # Set updated_by and updated_at

    db.session.commit()
    return jsonify({'message': 'Measuring unit updated successfully'})


@app.route('/measuring-units/<int:id>', methods=['DELETE'])
def delete_measuring_unit(id):
    unit = MeasuringUnit.query.get_or_404(id)
    db.session.delete(unit)
    db.session.commit()
    return jsonify({'message': 'Measuring unit deleted successfully'})

# ---- ITEM ENDPOINTS ----
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{
        'id': item.id,
        'name': item.item_name,
        'type': item.item_type.name,
        'category': item.item_category.name,
        'sales_price': item.sales_price,
        'created_by': item.created_by,
        'updated_by': item.updated_by,
        'created_at': item.created_at,
        'updated_at': item.updated_at,
        'business_id': item.business_id,
    } for item in items])


@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    item = Item(
        item_type_id=data['item_type_id'],
        category_id=data['category_id'],
        item_name=data['item_name'],
        sales_price=data['sales_price'],
        has_sales_price_including_tax=data.get('has_sales_price_including_tax', False),
        purchase_price=data['purchase_price'],
        gst_tax_rate=data['gst_tax_rate'],
        measuring_unit_id=data['measuring_unit_id'],
        opening_stock=data['opening_stock'],
        item_code=data['item_code'],
        hsn_code=data.get('hsn_code'),
        enable_low_quantity_warning=data.get('enable_low_quantity_warning', False),
        description=data.get('description'),
    )
    set_created_fields(item)  # Set created_by and created_at

    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item created successfully'}), 201


@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    item = Item.query.get_or_404(id)
    item.item_type_id = data['item_type_id']
    item.category_id = data['category_id']
    item.item_name = data['item_name']
    item.sales_price = data['sales_price']
    item.has_sales_price_including_tax = data.get('has_sales_price_including_tax', False)
    item.purchase_price = data['purchase_price']
    item.gst_tax_rate = data['gst_tax_rate']
    item.measuring_unit_id = data['measuring_unit_id']
    item.opening_stock = data['opening_stock']
    item.item_code = data['item_code']
    item.hsn_code = data.get('hsn_code')
    item.enable_low_quantity_warning = data.get('enable_low_quantity_warning', False)
    item.description = data.get('description')
    set_updated_fields(item)  # Set updated_by and updated_at

    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})


@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})

# ---- ITEM IMAGE ENDPOINTS ----
@app.route('/item-images', methods=['POST'])
def upload_item_image():
    data = request.json
    image = ItemImage(
        item_id=data['item_id'],
        image=data['image'],  # Assuming image is sent as binary or base64
    )
    db.session.add(image)
    db.session.commit()
    return jsonify({'message': 'Image uploaded successfully'}), 201


@app.route('/item-images/<int:id>', methods=['DELETE'])
def delete_item_image(id):
    image = ItemImage.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Image deleted successfully'})