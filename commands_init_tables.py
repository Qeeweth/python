""" create tables in the PostgreSQL database"""
commands_init_tables = (
    """
    CREATE TABLE IF NOT EXISTS tag (
        id uuid PRIMARY KEY,
        tag VARCHAR(255) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS info (
        id uuid PRIMARY KEY,
        description VARCHAR(5000) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS tag_info_merge (
        id uuid PRIMARY KEY,
        tag_id uuid NOT NULL constraint fk_merge_tag_id references tag, 
        info_id uuid NOT NULL constraint fk_merge_info_id references info
    )
    """
)
