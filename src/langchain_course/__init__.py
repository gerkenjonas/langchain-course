from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    information = """ Iron Man (deutsch etwa „eiserner Mann“, „Eisen-Mann“, in den ersten deutschen Veröffentlichungen „Der Eiserne“) ist eine Comicfigur der Marvel Comics. Erschaffen wurde sie von Stan Lee und Larry Lieber sowie den Zeichnern Don Heck und Jack Kirby. Ihr erster Auftritt war in dem Comic Tales of Suspense #39 im März 1963. 1968 erhielt sie eine eigene Reihe mit dem Titel Iron Man, die bis 1996 fortgesetzt wurde. Iron Mans Rüstung ist rot-golden und mit modernster Technik ausgestattet, wie zum Beispiel Plasmastrahlen.Iron Man ist das Alter Ego des Multimilliardärs und genialen Erfinders Anthony Edward „Tony“ Stark. Dieser übernimmt den Familienbetrieb Stark Industries, nachdem seine Eltern bei einem Autounfall ums Leben gekommen sind. Stark Industries ist ein Technologie-Konzern, der unter anderem im Auftrag der US-Regierung Waffensysteme entwickelt. Während einer Vorstellung seiner Erfindungen, welche im Vietnamkrieg eingesetzt werden, wird Stark bei einer Bombenexplosion verletzt und von den Nordvietnamesen gefangen genommen. Drei Granatsplitter verletzen ihn sehr nahe an seinem Herzen. Der Warlord Wong-Chu verspricht die Freilassung, wenn Stark für die Nordvietnamesen arbeitet.

    Zusammen mit Ho Yinsen, einem ebenfalls in Gefangenschaft befindlichen Nobelpreisträger für Physik, entwickelt Stark seine erste Iron-Man-Rüstung (Mark One), ein schwer gepanzertes Exoskelett. Dieses gibt Stark einerseits große Kampfkraft, andererseits ist es für ihn überlebenswichtig, da es den Metallsplitter in seinem Körper durch einen eingebauten Elektromagneten zurückhält und es ihm erlaubt, aus dem Lager zu fliehen. Er wird von seinem Freund James Rhodes gerettet. Zurück in den Vereinigten Staaten, gibt Tony Stark Iron Man als seinen Bodyguard aus und lebt zwei Identitäten.

    Während Iron Man in den ersten Jahren hauptsächlich gegen kommunistische Gegner, korrupte Geschäftskonkurrenten oder Terrororganisationen wie HYDRA und insbesondere A.I.M. (Advanced Idea Mechanic) kämpft, die an der Stark-Technologie und zumal an den Iron-Man-Rüstungen interessiert sind, zieht sich Stark aufgrund seiner Erfahrungen in Vietnam aus dem Waffengeschäft zurück und beginnt mit der Entwicklung des ARK-Reaktors als sauberer alternativer Energiequelle, um so Kriegen um knapper werdende Rohstoffe entgegenzuwirken. Er gründet verschiedene Wohltätigkeitsorganisationen wie die nach seiner Mutter benannte Maria-Stark-Stiftung. Seitdem gilt Tony Stark als Philanthrop. Iron Man ist ein Gründungsmitglied der Avengers (Rächer). Dieser Vereinigung von Superhelden stellt er über die Jahre unter anderem die Unterkunft, das Rächer-Hauptquartier, zur Verfügung.

    Tony Stark ist ein technisch versierter und erfinderischer Geschäftsmann. Gleichzeitig hat er aber auch persönliche Probleme wie seinen anhaltenden Narzissmus und seinen Gottkomplex, zudem gesundheitliche wie eine Palladiumvergiftung durch den Ark-Reaktor in seiner Brust, der die Granatsplitter von seinem Herzen fernhält. Diese Vergiftung zwingt ihn sogar zeitweilig, die Iron-Man-Rüstung abzulegen. Sie wird daraufhin von seinem Freund James Rhodes getragen. Rhodes erhält später seine eigene Rüstung mit der Iron-Man-Technologie und wird zum Superhelden namens War Machine, welcher an der Seite von Tony Stark kämpft. Tony kann wieder als Iron Man kämpfen, da er durch seinen toten Vater ein „neues“ Element entdeckt. Dieses ermöglicht es ihm, die Rüstung ohne weitere gesundheitliche Probleme zu tragen.

    Tony Starks fiktives Vermögen wird auf etwa 10[1] bis 50 Milliarden US-Dollar geschätzt. Er zählt damit zu den reichsten fiktiven Figuren der Welt.
    """

    summary_template = """
    die Informationen {information} zusammenfassen.
    In 3 Sätzen wiedergeben.

    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )
    llm = ChatGoogleGenerativeAI(model="google_genai", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response)

if __name__ == "__main__":
    main()