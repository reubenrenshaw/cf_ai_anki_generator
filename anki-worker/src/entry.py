from workers import Response, WorkerEntrypoint
from AnkiGenerator import create_anki_deck
import io


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        data = await request.json()
        try:
            package = create_anki_deck(data.get("Name"), data.get("Terms"))
            output = io.BytesIO()
            package.write_to_file(output)
            binary_data = output.getvalue()
        except Exception as e:
            return Response(f"Error: {str(e)}", status=500)
        headers = {
            "Content-Type": "application/zip",
            "Access-Control-Allow-Origin": "*"
        }

        return Response(binary_data, headers=headers)
