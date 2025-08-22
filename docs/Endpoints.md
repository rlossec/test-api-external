# Endpoints

## 1. Tools

### CRUD TOOLS

GET `tools/`

**Réponse attendue**
```json
{
  "data": [
    {
      "id": 1,
      "name": "Slack",
      "description": "Team messaging platform",
      "vendor": "Slack Technologies",
      "category": "Communication", 
      "monthly_cost": 8.00,
      "owner_department": "Engineering",
      "status": "active",
      "website_url": "https://slack.com",
      "active_users_count": 25,
      "created_at": "2025-05-01T09:00:00Z"
    }
  ],
  "total": 20,
  "filtered": 15,
  "filters_applied": {
    "department": "Engineering", 
    "status": "active"
  }
}
```

POST `tools/`

**Réponse attendue**
```json
{
  "id": 5,
  "name": "Confluence", 
  "description": "Team collaboration and documentation",
  "vendor": "Atlassian",
  "website_url": "https://confluence.atlassian.com",
  "category": "Development",
  "monthly_cost": 5.50,
  "owner_department": "Engineering",
  "status": "active",
  "active_users_count": 9,
  "total_monthly_cost": 49.50,
  "created_at": "2025-05-01T09:00:00Z",
  "updated_at": "2025-05-01T09:00:00Z",
  "usage_metrics": {
    "last_30_days": {
      "total_sessions": 127,
      "avg_session_minutes": 45
    }
  }
}
```
GET `tools/<tool_id>/`

**body**
```json
{
  "name": "Linear",
  "description": "Issue tracking and project management",
  "vendor": "Linear", 
  "website_url": "https://linear.app",
  "category_id": 2,
  "monthly_cost": 8.00,
  "owner_department": "Engineering"
}
```

**Réponse attendue**
```json
{
  "id": 21,
  "name": "Linear",
  "description": "Issue tracking and project management", 
  "vendor": "Linear",
  "website_url": "https://linear.app",
  "category": "Development",
  "monthly_cost": 8.00,
  "owner_department": "Engineering", 
  "status": "active",
  "active_users_count": 0,
  "created_at": "2025-08-20T14:30:00Z",
  "updated_at": "2025-08-20T14:30:00Z"
}
```
PUT `tools/<tool_id>/`  
**body**
```json
{
  "description": "Issue tracking and project management",
  "monthly_cost": 7.00,
  "status": "deprecated"
}
```
**Réponse attendue**
```json
{
  "id": 5,
  "name": "Confluence",
  "description": "Updated description after renewal",
  "vendor": "Atlassian", 
  "website_url": "https://confluence.atlassian.com",
  "category": "Development",
  "monthly_cost": 7.00,
  "owner_department": "Engineering",
  "status": "deprecated", 
  "active_users_count": 9,
  "created_at": "2025-05-01T09:00:00Z",
  "updated_at": "2025-08-20T15:45:00Z"
}
```

## 2. Analytics

### Répartition coût par département
GET `analytics/department-costs`

Exemple de réponse
```json
{
  "data": [
    {
      "department": "Engineering",
      "total_cost": 890.50,
      "tools_count": 12,
      "total_users": 45,
      "average_cost_per_tool": 74.21,
      "cost_percentage": 36.2
    },
    {
      "department": "Sales", 
      "total_cost": 456.75,
      "tools_count": 6,
      "total_users": 18,
      "average_cost_per_tool": 76.13,
      "cost_percentage": 18.6
    }
  ],
  "summary": {
    "total_company_cost": 2450.80,
    "departments_count": 6,
    "most_expensive_department": "Engineering"
  }
}
```

Tables requises : 
Sur Tools
- tools_count : SUM GroupBy owner_department
Sur TrackingCost 
- total_company_cost : SUM colonne total_monthly_cost
Sur Jointure entre Tools et TackingCost (avec tool_id)
- total_cost : SUM total_monthly_cost
- total_users : SUM active




### Top outils coûteux
GET `analytics/expensive-tools`

Réponse attendue :
```json
{
  "data": [
    {
      "id": 15,
      "name": "Enterprise CRM",
      "monthly_cost": 199.99,
      "active_users_count": 12,
      "cost_per_user": 16.67,
      "department": "Sales",
      "vendor": "BigCorp",
      "efficiency_rating": "low"
    }
  ],
  "analysis": {
    "total_tools_analyzed": 18,
    "avg_cost_per_user_company": 12.45,
    "potential_savings_identified": 345.50
  }
}
```

### Répartition des outils par catégories
GET `analytics/tools-by-category`

Réponse attendue :
```json
{
  "data": [
    {
      "category_name": "Development",
      "tools_count": 8,
      "total_cost": 650.00,
      "total_users": 67,
      "percentage_of_budget": 26.5,
      "average_cost_per_user": 9.70
    },
    {
      "category_name": "Communication",
      "tools_count": 5,
      "total_cost": 240.50,
      "total_users": 89, 
      "percentage_of_budget": 9.8,
      "average_cost_per_user": 2.70
    }
  ],
  "insights": {
    "most_expensive_category": "Development",
    "most_efficient_category": "Communication"
  }
}
```

### Outils sous-utilisés
GET `analytics/low-usage-tools`

```json
{
  "data": [
    {
      "id": 23,
      "name": "Specialized Analytics",
      "monthly_cost": 89.99,
      "active_users_count": 2,
      "cost_per_user": 45.00,
      "department": "Marketing",
      "vendor": "SmallVendor",
      "warning_level": "high",
      "potential_action": "Consider canceling or downgrading"
    }
  ],
  "savings_analysis": {
    "total_underutilized_tools": 5,
    "potential_monthly_savings": 287.50,
    "potential_annual_savings": 3450.00
  }
}
```

### Analyse fournisseurs
GET `analytics/vendor-summary`

```json
{
  "data": [
    {
      "vendor": "Google",
      "tools_count": 4,
      "total_monthly_cost": 234.50,
      "total_users": 67,
      "departments": "Engineering,Sales,Marketing",
      "average_cost_per_user": 3.50,
      "vendor_efficiency": "excellent"
    }
  ],
  "vendor_insights": {
    "most_expensive_vendor": "BigCorp",
    "most_efficient_vendor": "Google",
    "single_tool_vendors": 8
  }
}
```