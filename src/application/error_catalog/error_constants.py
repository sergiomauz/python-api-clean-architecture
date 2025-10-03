from .error_tuple import ErrorTuple
    
    
class ErrorConstants:
    GENERIC_00000 = "G00000"

    # Id
    ID_FORMAT00001 = ErrorTuple("Id-F00001", "id", "'id' can not be null.")
    ID_FORMAT00002 = ErrorTuple("Id-F00002", "id", "'id' must be greater than 0.")    
    
    # Uuid
    UUID_FORMAT00001 = ErrorTuple("Uuid-F00001", "id", "'id' must be a valid UUID.")
    
    # Ids
    IDS_FORMAT00001 = ErrorTuple("Ids-F00001", "ids", "List must not be null.")
    IDS_FORMAT00002 = ErrorTuple("Ids-F00002", "ids", "List must not be empty.")
    IDS_FORMAT00003 = ErrorTuple("Ids-F00003", "ids", "List must not have repeated elements.")
    IDS_FORMAT00004 = ErrorTuple("Ids-F00004", "ids", "All elements must be greater than 0.")

    # Uuids
    UUIDS_FORMAT00001 = ErrorTuple("Uuids-F00001", "ids", "List must not be null.")    
    UUIDS_FORMAT00002 = ErrorTuple("Uuids-F00002", "ids", "List must not be empty.")
    UUIDS_FORMAT00003 = ErrorTuple("Uuids-F00003", "ids", "List must not have repeated elements.")
    UUIDS_FORMAT00004 = ErrorTuple("Uuids-F00004", "ids", "All elements must be valids UUID.")

    # BasicSearch
    BASIC_SEARCH_FORMAT00001 = ErrorTuple("BasicSearch-F00001", "text_filter", "'text_filter' must have 3 or more characters.")
        
    # Paginated    
    PAGINATED_FORMAT00001 = ErrorTuple("Paginated-F00001", "page_size", "'page_size' must be between 0 and 300.")
    PAGINATED_FORMAT00002 = ErrorTuple("Paginated-F00002", "current_page", "'current_page' must be greater than 0.")
    
    # CreateCategory
    CREATE_CATEGORY_FORMAT00001 = ErrorTuple("CreateCategory-F00001", "name", "'name' must have between 3 and 75 characters.")
    CREATE_CATEGORY_FORMAT00002 = ErrorTuple("CreateCategory-F00002", "description", "'description' must have between 3 and 150 characters.")
    CREATE_CATEGORY_CONTENT00001 = ErrorTuple("CreateCategory-C00001", "name", "This name already exists. Try another name.")
    
    # UpdateCategory
    UPDATE_CATEGORY_FORMAT00001 = ErrorTuple("UpdateCategory-F00001", "name", "'name' must have between 3 and 75 characters")
    UPDATE_CATEGORY_FORMAT00002 = ErrorTuple("UpdateCategory-F00002", "description", "'description' must have between 3 and 150 characters.")
    UPDATE_CATEGORY_CONTENT00001 = ErrorTuple("UpdateCategory-C00001", "id", "This category does not exist.")
    UPDATE_CATEGORY_CONTENT00002 = ErrorTuple("UpdateCategory-C00002", "name", "This name already exists. Try another name.")
    
    # GetCategoryById
    GET_CATEGORY_BY_ID_CONTENT00001 = ErrorTuple("GetCategoryById-C00001", "id", "This category does not exist.")
    
    # SearchCategoriesByObjectFiltering
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00001 = ErrorTuple("SearchCategoriesByObjectFiltering-F00001", "name", "'name' must be a valid string or an array strings")
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00002 = ErrorTuple("SearchCategoriesByObjectFiltering-F00002", "name", "'name' must have between 1 and 75 characters")
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00003 = ErrorTuple("SearchCategoriesByObjectFiltering-F00003", "name", "'{operator}' is not a valid filtering operator for '{operand}'.")
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00004 = ErrorTuple("SearchCategoriesByObjectFiltering-F00004", "description", "'description' must be a valid string or an array strings")
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00005 = ErrorTuple("SearchCategoriesByObjectFiltering-F00005", "description", "'description' must have between 1 and 150 characters.")
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00006 = ErrorTuple("SearchCategoriesByObjectFiltering-F00006", "description", "'{operator}' is not a valid filtering operator for '{operand}'.")
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00007 = ErrorTuple("SearchCategoriesByObjectFiltering-F00007", "created_at", "'created_at' must be a valid string datetime or an array string datetimes")
    SEARCH_CATEGORIES_BY_OBJECT_FILTERING_FORMAT00008 = ErrorTuple("SearchCategoriesByObjectFiltering-F00008", "created_at", "'{operator}' is not a valid filtering operator for '{operand}'.")
    
    # SearchCategoriesByObjectOrdering
    SEARCH_CATEGORIES_BY_OBJECT_ORDERING_FORMAT00001 = ErrorTuple("SearchCategoriesByObjectOrdering-F00001", "name", "'{order_by}' is not a valid ordering operator.")
    SEARCH_CATEGORIES_BY_OBJECT_ORDERING_FORMAT00002 = ErrorTuple("SearchCategoriesByObjectOrdering-F00002", "description", "'{order_by}' is not a valid ordering operator.")
    SEARCH_CATEGORIES_BY_OBJECT_ORDERING_FORMAT00003 = ErrorTuple("SearchCategoriesByObjectOrdering-F00003", "created_at", "'{order_by}' is not a valid ordering operator.")
    
    # CreateProduct
    CREATE_PRODUCT_FORMAT00001 = ErrorTuple("CreateProduct-F00001", "category_id", "'category_id' must be a valid integer greater than 0.")
    CREATE_PRODUCT_FORMAT00002 = ErrorTuple("CreateProduct-F00002", "code", "'code' must have between 5 and 10 characters.")
    CREATE_PRODUCT_FORMAT00003 = ErrorTuple("CreateProduct-F00003", "name", "'name' must have between 3 and 75 characters.")
    CREATE_PRODUCT_FORMAT00004 = ErrorTuple("CreateProduct-F00004", "description", "'description' must have between 3 and 150 characters.")
    CREATE_PRODUCT_CONTENT00001 = ErrorTuple("CreateProduct-C00001", "category_id", "This category does not exist.")
    CREATE_PRODUCT_CONTENT00002 = ErrorTuple("CreateProduct-C00002", "code", "This code already exists. Try another code.")
    
    # UpdateProduct
    UPDATE_PRODUCT_FORMAT00001 = ErrorTuple("UpdateProduct-F00001", "category_id", "'category_id' must be a valid integer greater than 0.")
    UPDATE_PRODUCT_FORMAT00002 = ErrorTuple("UpdateProduct-F00002", "code", "'code' must have between 5 and 10 characters")
    UPDATE_PRODUCT_FORMAT00003 = ErrorTuple("UpdateProduct-F00003", "name", "'name' must have between 3 and 75 characters.")
    UPDATE_PRODUCT_FORMAT00004 = ErrorTuple("UpdateProduct-F00004", "description", "'description' must have between 3 and 150 characters.")
    UPDATE_PRODUCT_CONTENT00001 = ErrorTuple("CreateProduct-C00001", "id", "This product does not exist.")
    UPDATE_PRODUCT_CONTENT00002 = ErrorTuple("CreateProduct-C00002", "code", "This code already exists. Try another code.")
    UPDATE_PRODUCT_CONTENT00003 = ErrorTuple("CreateProduct-C00003", "category_id", "This category does not exist.")        
    
    # GetProductById
    GET_PRODUCT_BY_ID_CONTENT00001 = ErrorTuple("GetProductById-C00001", "id", "This product does not exist.")
    
    # SearchProductsByObjectOrdering
    SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00001 = ErrorTuple("SearchProductsByObjectOrdering-F00001", "code", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00002 = ErrorTuple("SearchProductsByObjectOrdering-F00002", "name", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00003 = ErrorTuple("SearchProductsByObjectOrdering-F00003", "category", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00004 = ErrorTuple("SearchProductsByObjectOrdering-F00004", "description", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PRODUCTS_BY_OBJECT_ORDERING_FORMAT00005 = ErrorTuple("SearchProductsByObjectOrdering-F00005", "created_at", "'{order_by}' is not a valid ordering operator.")    
    
    # SearchProductsByObjectFiltering    
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00001 = ErrorTuple("SearchProductsByObjectFiltering-F00001", "code", "'code' must be a valid string or an array strings")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00002 = ErrorTuple("SearchProductsByObjectFiltering-F00002", "code", "'code' must have between 1 and 75 characters")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00003 = ErrorTuple("SearchProductsByObjectFiltering-F00003", "code", "'{operator}' is not a valid filtering operator for '{operand}'")    
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00004 = ErrorTuple("SearchProductsByObjectFiltering-F00004", "name", "'name' must be a valid string or an array strings")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00005 = ErrorTuple("SearchProductsByObjectFiltering-F00005", "name", "'name' must have between 1 and 75 characters")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00006 = ErrorTuple("SearchProductsByObjectFiltering-F00006", "name", "'{operator}' is not a valid filtering operator for '{operand}'")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00007 = ErrorTuple("SearchProductsByObjectFiltering-F00007", "category", "'category' must be a valid string or an array strings")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00008 = ErrorTuple("SearchProductsByObjectFiltering-F00008", "category", "'category' must have between 1 and 75 characters")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00009 = ErrorTuple("SearchProductsByObjectFiltering-F00009", "category", "'{operator}' is not a valid filtering operator for '{operand}'")    
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00010 = ErrorTuple("SearchProductsByObjectFiltering-F00010", "description", "'description' must be a valid string or an array strings")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00011 = ErrorTuple("SearchProductsByObjectFiltering-F00011", "description", "'description' must have between 1 and 75 characters")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00012 = ErrorTuple("SearchProductsByObjectFiltering-F00012", "description", "'{operator}' is not a valid filtering operator for '{operand}'")            
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00013 = ErrorTuple("SearchProductsByObjectFiltering-F00013", "created_at", "'created_at' must be a valid string datetime or an array string datetimes")
    SEARCH_PRODUCTS_BY_OBJECT_FILTERING_FORMAT00014 = ErrorTuple("SearchProductsByObjectFiltering-F00014", "created_at", "'{operator}' is not a valid filtering operator for '{operand}'.")
    
    # CreatePartner
    CREATE_PARTNER_FORMAT00001 = ErrorTuple("CreatePartner-F00001", "code", "'code' must have 10 characters.")
    CREATE_PARTNER_FORMAT00002 = ErrorTuple("CreatePartner-F00002", "name", "'name' must have between 5 and 350 characters.")
    CREATE_PARTNER_FORMAT00003 = ErrorTuple("CreatePartner-F00003", "contact", "'contact' must have between 3 and 200 characters.")
    CREATE_PARTNER_FORMAT00004 = ErrorTuple("CreatePartner-F00004", "phone", "'phone' must be a valid phone number.")
    CREATE_PARTNER_FORMAT00005 = ErrorTuple("CreatePartner-F00005", "address", "'address' must have between 5 and 500 characters.")    
    CREATE_PARTNER_FORMAT00006 = ErrorTuple("CreatePartner-F00006", "email", "'email' must be a valid email address.")
    CREATE_PARTNER_CONTENT00001 = ErrorTuple("CreatePartner-C00001", "code", "This code already exists. Try another code.")
    
    # UpdatePartner
    UPDATE_PARTNER_FORMAT00001 = ErrorTuple("UpdatePartner-F00001", "code", "'code' must have 10 characters.")
    UPDATE_PARTNER_FORMAT00002 = ErrorTuple("UpdatePartner-F00002", "name", "'name' must have between 5 and 350 characters.")
    UPDATE_PARTNER_FORMAT00003 = ErrorTuple("UpdatePartner-F00003", "contact", "'contact' must have between 3 and 200 characters.")
    UPDATE_PARTNER_FORMAT00004 = ErrorTuple("UpdatePartner-F00004", "phone", "'phone' must be a valid phone number.")
    UPDATE_PARTNER_FORMAT00005 = ErrorTuple("UpdatePartner-F00005", "address", "'address' must have between 5 and 500 characters.")    
    UPDATE_PARTNER_FORMAT00006 = ErrorTuple("UpdatePartner-F00006", "email", "'email' must be a valid email address.")    
    UPDATE_PARTNER_CONTENT00001 = ErrorTuple("UpdatePartner-C00001", "id", "This partner does not exist.")
    UPDATE_PARTNER_CONTENT00002 = ErrorTuple("UpdatePartner-C00002", "code", "This code already exists. Try another code.")
    
    # GetPartnerById
    GET_PARTNER_BY_ID_CONTENT00001 = ErrorTuple("GetPartnerById-C00001", "id", "This partner does not exist.")
    
    # SearchPartnersByObjectOrdering
    SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00001 = ErrorTuple("SearchPartnersByObjectOrdering-F00001", "name", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00002 = ErrorTuple("SearchPartnersByObjectOrdering-F00002", "contact", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00003 = ErrorTuple("SearchPartnersByObjectOrdering-F00003", "phone", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00004 = ErrorTuple("SearchPartnersByObjectOrdering-F00004", "address", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00005 = ErrorTuple("SearchPartnersByObjectOrdering-F00005", "email", "'{order_by}' is not a valid ordering operator.")
    SEARCH_PARTNERS_BY_OBJECT_ORDERING_FORMAT00006 = ErrorTuple("SearchPartnersByObjectOrdering-F00006", "created_at", "'{order_by}' is not a valid ordering operator.")

    # SearchPartnersByObjectFiltering
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00001 = ErrorTuple("SearchPartnersByObjectFiltering-F00001", "code", "'code' must be a valid string or an array strings")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00002 = ErrorTuple("SearchPartnersByObjectFiltering-F00002", "code", "'code' must have between 1 and 15 characters")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00003 = ErrorTuple("SearchPartnersByObjectFiltering-F00003", "code", "'{operator}' is not a valid filtering operator for '{operand}'")    
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00004 = ErrorTuple("SearchPartnersByObjectFiltering-F00004", "name", "'name' must be a valid string or an array strings")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00005 = ErrorTuple("SearchPartnersByObjectFiltering-F00005", "name", "'name' must have between 1 and 75 characters")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00006 = ErrorTuple("SearchPartnersByObjectFiltering-F00006", "name", "'{operator}' is not a valid filtering operator for '{operand}'")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00007 = ErrorTuple("SearchPartnersByObjectFiltering-F00007", "contact", "'contact' must be a valid string or an array strings")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00008 = ErrorTuple("SearchPartnersByObjectFiltering-F00008", "contact", "'contact' must have between 1 and 75 characters")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00009 = ErrorTuple("SearchPartnersByObjectFiltering-F00009", "contact", "'{operator}' is not a valid filtering operator for '{operand}'")    
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00010 = ErrorTuple("SearchPartnersByObjectFiltering-F00010", "phone", "'phone' must be a valid string or an array strings")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00011 = ErrorTuple("SearchPartnersByObjectFiltering-F00011", "phone", "'phone' must have between 1 and 15 characters")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00012 = ErrorTuple("SearchPartnersByObjectFiltering-F00012", "phone", "'{operator}' is not a valid filtering operator for '{operand}'")        
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00013 = ErrorTuple("SearchPartnersByObjectFiltering-F00013", "address", "'address' must be a valid string or an array strings")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00014 = ErrorTuple("SearchPartnersByObjectFiltering-F00014", "address", "'address' must have between 1 and 75 characters")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00015 = ErrorTuple("SearchPartnersByObjectFiltering-F00015", "address", "'{operator}' is not a valid filtering operator for '{operand}'")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00016 = ErrorTuple("SearchPartnersByObjectFiltering-F00016", "email", "'email' must be a valid string or an array strings")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00017 = ErrorTuple("SearchPartnersByObjectFiltering-F00017", "email", "'email' must have between 1 and 75 characters")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00018 = ErrorTuple("SearchPartnersByObjectFiltering-F00018", "email", "'{operator}' is not a valid filtering operator for '{operand}'")    
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00019 = ErrorTuple("SearchPartnersByObjectFiltering-F00019", "created_at", "'created_at' must be a valid string datetime or an array string datetimes")
    SEARCH_PARTNERS_BY_OBJECT_FILTERING_FORMAT00020 = ErrorTuple("SearchPartnersByObjectFiltering-F00020", "created_at", "'{operator}' is not a valid filtering operator for '{operand}'.")    
    
    # CreateMovement
    CREATE_MOVEMENT_FORMAT00001 = ErrorTuple("CreateMovement-F00001", "partner_id", "'partner_id' must be a valid integer greater than 0.")
    CREATE_MOVEMENT_FORMAT00002 = ErrorTuple("CreateMovement-F00002", "product_id", "'product_id' must be a valid integer greater than 0.")
    CREATE_MOVEMENT_FORMAT00003 = ErrorTuple("CreateMovement-F00003", "movement_date", "'movement_date' must be a valid datetime.")
    CREATE_MOVEMENT_FORMAT00004 = ErrorTuple("CreateMovement-F00004", "quantity", "'quantity' must be a valid number greater than 0.")
    CREATE_MOVEMENT_FORMAT00005 = ErrorTuple("CreateMovement-F00005", "movement_type", "'{movement_type}' is not a valid movement type.")    
    CREATE_MOVEMENT_CONTENT00001 = ErrorTuple("CreatePartner-C00001", "product_id", "This product does not exist.")
    CREATE_MOVEMENT_CONTENT00002 = ErrorTuple("CreatePartner-C00002", "partner_id", "This partner does not exist.")
    
    # GetMovementById
    GET_MOVEMENT_BY_ID_CONTENT00001 = ErrorTuple("GetMovementById-C00001", "id", "This movement does not exist.")
    
    # SearchMovementsByObjectOrdering
    SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00001 = ErrorTuple("SearchMovementsByObjectOrdering-F00001", "partner", "'{order_by}' is not a valid ordering operator.")
    SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00002 = ErrorTuple("SearchMovementsByObjectOrdering-F00002", "product", "'{order_by}' is not a valid ordering operator.")
    SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00003 = ErrorTuple("SearchMovementsByObjectOrdering-F00003", "quantity", "'{order_by}' is not a valid ordering operator.")
    SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00004 = ErrorTuple("SearchMovementsByObjectOrdering-F00004", "movement_type", "'{order_by}' is not a valid ordering operator.")
    SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00005 = ErrorTuple("SearchMovementsByObjectOrdering-F00005", "movement_date", "'{order_by}' is not a valid ordering operator.")
    SEARCH_MOVEMENTS_BY_OBJECT_ORDERING_FORMAT00006 = ErrorTuple("SearchMovementsByObjectOrdering-F00006", "created_at", "'{order_by}' is not a valid ordering operator.")
    
    # SearchMovementsByObjectFiltering
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00001 = ErrorTuple("SearchMovementsByObjectFiltering-F00001", "partner", "'partner' must be a valid string or an array strings")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00002 = ErrorTuple("SearchMovementsByObjectFiltering-F00002", "partner", "'partner' must have between 1 and 75 characters")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00003 = ErrorTuple("SearchMovementsByObjectFiltering-F00003", "partner", "'{operator}' is not a valid filtering operator for '{operand}'")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00004 = ErrorTuple("SearchMovementsByObjectFiltering-F00004", "product", "'product' must be a valid string or an array strings")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00005 = ErrorTuple("SearchMovementsByObjectFiltering-F00005", "product", "'product' must have between 1 and 75 characters")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00006 = ErrorTuple("SearchMovementsByObjectFiltering-F00006", "product", "'{operator}' is not a valid filtering operator for '{operand}'.")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00007 = ErrorTuple("SearchMovementsByObjectFiltering-F00007", "quantity", "'quantity' must be a valid number or an array of numbers")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00008 = ErrorTuple("SearchMovementsByObjectFiltering-F00008", "quantity", "'quantity' must be greater than 0")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00009 = ErrorTuple("SearchMovementsByObjectFiltering-F00009", "quantity", "'{operator}' is not a valid filtering operator for '{operand}'.")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00010 = ErrorTuple("SearchMovementsByObjectFiltering-F00010", "movement_type", "'movement_type' must be a valid string or an array strings")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00011 = ErrorTuple("SearchMovementsByObjectFiltering-F00011", "movement_type", "'movement_type' must be a valid movement type")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00012 = ErrorTuple("SearchMovementsByObjectFiltering-F00012", "movement_type", "'{operator}' is not a valid filtering operator for '{operand}'")    
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00013 = ErrorTuple("SearchCategoriesByObjectFiltering-F00013", "movement_date", "'movement_date' must be a valid string datetime or an array string datetimes")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00014 = ErrorTuple("SearchCategoriesByObjectFiltering-F00014", "movement_date", "'{operator}' is not a valid filtering operator for '{operand}'.")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00015 = ErrorTuple("SearchCategoriesByObjectFiltering-F00015", "created_at", "'created_at' must be a valid string datetime or an array string datetimes")
    SEARCH_MOVEMENTS_BY_OBJECT_FILTERING_FORMAT00016 = ErrorTuple("SearchCategoriesByObjectFiltering-F00016", "created_at", "'{operator}' is not a valid filtering operator for '{operand}'.")