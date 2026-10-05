from typing import List, Dict, Any
from .database import get_connection

def search_legal_knowledge(query: str, lang: str = "en", category: str = None) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    
    if category:
        cursor.execute("SELECT * FROM knowledge_base WHERE category = ?", (category,))
    elif query.strip():
        search_pattern = f"%{query.strip()}%"
        cursor.execute("""
            SELECT * FROM knowledge_base 
            WHERE category LIKE ? 
               OR title_en LIKE ? OR title_hi LIKE ? OR title_od LIKE ?
               OR summary_en LIKE ? OR summary_hi LIKE ? OR summary_od LIKE ?
               OR relevant_acts LIKE ? OR legal_sections LIKE ?
        """, (search_pattern, search_pattern, search_pattern, search_pattern,
              search_pattern, search_pattern, search_pattern,
              search_pattern, search_pattern))
    else:
        cursor.execute("SELECT * FROM knowledge_base")

    rows = cursor.fetchall()
    conn.close()

    results = []
    for r in rows:
        results.append({
            "id": r["id"],
            "category": r["category"],
            "title": r[f"title_{lang}"] if f"title_{lang}" in r.keys() else r["title_en"],
            "title_en": r["title_en"],
            "title_hi": r["title_hi"],
            "title_od": r["title_od"],
            "summary": r[f"summary_{lang}"] if f"summary_{lang}" in r.keys() else r["summary_en"],
            "summary_en": r["summary_en"],
            "summary_hi": r["summary_hi"],
            "summary_od": r["summary_od"],
            "legal_sections": r["legal_sections"],
            "remedies": r["remedies"],
            "procedure_steps": r["procedure_steps"],
            "relevant_acts": r["relevant_acts"],
            "helpline": r["helpline"]
        })
    return results

def get_category_knowledge(category: str) -> Dict[str, Any]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM knowledge_base WHERE category = ?", (category,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return {}
