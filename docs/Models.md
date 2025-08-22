# Modèles

Toutes les tables ont les champs, created_at, updated_at.  
Dans toolsmanagement, un modèle de base permet d'ajouter d'autres éléments si nécessaire.


## 1. Catégorie

Les catégories sont remplies initialement.

**Champs**
- name
- description
- color_hex

**Choix** RAS ✅  
**A discuter** : RAS ✅

## 2. User

Les utilisateurs s'enregistrent et alimentent leurs informations
vs Un admin remplit leurs informations ?

**Champs**
- first_name
- last_name
- username
- email
- department                (Enum : Department Choices)
- role                      (Enum : Admin/Manager/Employee)
- status                    (Enum : Active/Inactive/Removed)


**Choix**
- Conservation du modèle User initial de Django (first_name, last_name, username)

A discuter :
- Suppression d'username et l'email deviendrait l'identificant
- Unicité et obligation email
- Enum department : choix identiques avec outil, Tables ou refactoring pour n'avoir qu'une seule varaable
- status : booléen ?
- "Nom" vs "Prénom Nom" ?
- Ajouter de fausses données avec les statuts inactive et removed

## 3. Tool

**Champs**
- name
- description
- vendor
- category
- base_monthly_cost
- website_url
- owner_department
- status                  (Active/Trial/Deprecated)

**A discuter**
- Ajouter des outils avec les status Trial et Deprecated

**Choix**
- renommer monthly_cost en base_monthly_cost

## 4. Access Request

Se remplit en deux temps :
- demande d'accès de l'utilisateur
- validation par un manager

Champs :
- user_id
- tool_id
- business_justification
- status                  (Pending, Approved, Rejected)
- processed_by
- processing_notes
- requested_at -> created_at
~~- processed_at -> updated_at~~

**Propriétés**
- requested_at

**Méthodes**
- approve : procédure d'approbation
- reject : procédure de rejet

**Choix**

- requested_at en propriété pour accéder à created_at
~~- processed_at en propriété pour accéder à updated_at~~

A discuter :
- Ajouter des données avec les différents statuts

## 5. Tool Access

La table se remplit suite à la validation des access request

**Champs**
- user_id
- tool_id
- granted_at
- granted_by
- revoked_at
- revoked_by

**Propriétés**
- status
- is_active

**Méthodes**
- revoke_access

Choix :
 - suppression du champ status, déduit de la présence de revoked_at
 - unicité du couple user-tool

A discuter :
 - Ajouter des données avec des champs revoked_at et revoked_by

## 6. Usage Logs

**Champs**
- tool_id 
- user_id
- usage_minutes
- actions_count
- session_date


## 7. Cost tracking

On suppose qu'un manager remplit le coût final à la fin du mois.

**Champs**
- tool_id
- month_year
- total_monthly_cost

**Choix**
 - active_users_count en propriété et calculé via tool
 - ajouts de propriété base_monthly-cost et aditionnal_costs



### Ordre d'utilisation

**Préalables**
1. Entrée des catégories
2. Création des utilisateurs / Enregistrement
3. Création des outils  

**En continu**
1. Process des accès aux outils
2. Suivi des coûts

**Analytics**

### Endpoints :
- CRUD Catégorie
- CRUD User vs Authentication ?
- CRUD Tool 
- Endpoint Demande d'accès
- Endpoints approbation/rejet
- Endpoint d'enregistrement des activités
- Endpoints analytics