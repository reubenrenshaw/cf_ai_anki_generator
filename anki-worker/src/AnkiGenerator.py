import genanki
import random


def create_anki_deck(name: str, terms: list) -> genanki.Package:
    # 1. Use a stable Model ID or one based on the name
    model_id = random.randrange(1 << 30, 1 << 31)
    model = genanki.Model(
        model_id,
        'Simple Model',  # Changed from name to a static string for testing
        fields=[
            {'name': "Question"},
            {'name': "Answer"},
        ],
        templates=[
            {
                'name': 'Card',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    # 2. Create deck
    deck_id = random.randrange(1 << 30, 1 << 31)
    deck = genanki.Deck(deck_id, name or 'My Deck')

    # 3. Handle 'terms' as a List of Dicts (matching common JSON patterns)
    for item in terms:
        # Check if item is a dict (e.g., {"Question": "...", "Answer": "..."})
        # or a list/tuple (e.g. ["Question", "Answer"])
        if isinstance(item, dict):
            # Adapt these keys to match your frontend JSON
            q = item.get("front") or item.get("Question")
            a = item.get("back") or item.get("Answer")
        else:
            q, a = item

        note = genanki.Note(
            model=model,
            fields=[str(q), str(a)]
        )
        deck.add_note(note)

    return genanki.Package(deck)
