# Generated by Django 4.1.1 on 2022-11-22 05:52

from django.db import migrations, connection, transaction
from pydash import flatten


def add_names_for_latest_version(apps, schema_editor):
    import time
    start = time.time()
    """
    1. Populates LocalizedText with copy of names of Concept for its latest version.
    2. Concept and its latest version used to share names (and descriptions) using many-to-many (concepts_names).
    3. After this migration:
       - localized_texts will have new entries with concept_id as concept.latest_version.id
       - concepts_names will not have anything for any latest versions.
       - concepts_names will not have any duplicate localizedtext_id.
       - concepts_names for latest versions needs to be deleted for the next migration to populate concept_id in
         localized_texts. Latest versions and Concept itself uses the same localizedtext_id.
    """

    def get_statement():
        return "insert into localized_texts(concept_id, external_id, name, type, locale, locale_preferred, created_at) values "

    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    with connection.cursor() as cursor:
        cursor.execute("select id from concepts where is_latest_version=true;")
        concepts = cursor.fetchall()
        statement = get_statement()
        count = 0
        for concept in concepts:
            cursor.execute("select localizedtext_id from concepts_names where concept_id = %s", concept)
            locales = cursor.fetchall()
            for locale in locales:
                cursor.execute(
                    "select external_id, name, type, locale, locale_preferred, created_at from localized_texts where id = %s",
                    [locale]
                )
                _locale = cursor.fetchone()
                name = _locale[1].replace("'", "''")
                statement += f"({concept[0]}, '{_locale[0]}', '{name}', '{_locale[2]}', '{_locale[3]}', {_locale[4]}, '{_locale[5]}'),"
                count += 1
                if count == 10000:
                    if statement.endswith(','):
                        statement = statement[:-1] + ';'
                    print(f"Inserting {count}...")
                    cursor.execute(statement)
                    statement = get_statement()
                    count = 0

        if count > 0:
            if statement.endswith(','):
                statement = statement[:-1] + ';'

            print(f"Inserting Last {count}...")
            cursor.execute(statement)

        for concept_ids in chunks(flatten(concepts), 1000):
            print("Deleting...")
            cursor.execute(f'delete from concepts_names where concept_id in {tuple(concept_ids)}')

    print('Time: ', time.time() - start)


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('concepts', '0038_auto_20221122_0522'),
    ]

    operations = [
        migrations.RunPython(add_names_for_latest_version)
    ]
