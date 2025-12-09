import argparse
import mimetypes
import base64
import google.generativeai as genai

#Extracting values from images to use in user request
def load_image_b64(path):
    mime, _ = mimetypes.guess_type(path)
    if mime is None:
        mime = "image/jpeg"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    return mime, b64

def build_image_blocks(paths):
    blocks = []
    for path in paths:
        mime, b64 = load_image_b64(path)

        #building the user request images
        blocks.append({
            "mime_type": mime,
            "data": base64.b64decode(b64)
        })

        # print("blocks successful!")

    return blocks


def build_system_prompt():
    system_prompt = '''
Analyze chat tone/power/humor → return only the ideal, extremely humanized 1–2 line message that blends in and improves the vibe. No analysis text. Unclear → “Need clearer chat details.” Off-topic → “I specialize in chat analysis.”
'''
    return system_prompt


def main():

    genai.configure(api_key="INSERT_API_Key")

    model = genai.GenerativeModel("gemini-2.5-flash")

    parser = argparse.ArgumentParser(description="Anti-awkwardness bot")
    parser.add_argument("images", nargs="+", help="Paths to chat screenshots")
    args = parser.parse_args()

    # print("Images received:", args.images)

    # images being built into a list for gemini to process
    image_parts = build_image_blocks(args.images)

    system_prompt = build_system_prompt()

    final_input = [
        {"text": system_prompt},
        {"text": "User request: what do I say next?"}
    ]

    final_input.extend(image_parts)


    response = model.generate_content(
        final_input,
        safety_settings={"HARASSMENT": "BLOCK_NONE"}
    )

    print(response.text)


if __name__ == "__main__":
    main()
