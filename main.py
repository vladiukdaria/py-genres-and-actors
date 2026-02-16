from db.models import Genre, Actor


def main():
    # Create genres
    genres = [
        ("Western",),
        ("Action",),
        ("Dramma",),
    ]

    for (name,) in genres:
        Genre.objects.create(name=name)

    # Create actors
    actors = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]

    for first_name, last_name in actors:
        Actor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )

    # Update genre Dramma -> Drama
    genre = Genre.objects.get(name="Dramma")
    genre.name = "Drama"
    genre.save()

    # Update George Klooney -> George Clooney
    actor = Actor.objects.get(first_name="George", last_name="Klooney")
    actor.last_name = "Clooney"
    actor.save()

    # Update Kianu Reaves -> Keanu Reeves
    actor = Actor.objects.get(first_name="Kianu", last_name="Reaves")
    actor.first_name = "Keanu"
    actor.last_name = "Reeves"
    actor.save()

    # Delete genre Action
    Genre.objects.filter(name="Action").delete()

    # Delete all actresses with first_name Scarlett
    Actor.objects.filter(first_name="Scarlett").delete()

    # Return actors with last_name Smith ordered by first_name
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
