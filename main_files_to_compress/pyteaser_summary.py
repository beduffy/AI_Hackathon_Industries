from pyteaser import SummarizeUrl, Summarize
#url = 'http://www.huffingtonpost.com/2013/11/22/twitter-forward-secrecy_n_4326599.html'
#summaries = SummarizeUrl(url)



def summarise_text(title, text):
    title = 'Nightfall'

    #text = "Text messaging, or texting, is the act of composing and sending electronic messages, typically consisting of alphabetic and numeric characters, between two or more users of mobile phones, tablets, desktops/laptops, or other devices. Text messages may be sent over a cellular network, or may also be sent via an Internet connection. The term originally referred to messages sent using the Short Message Service (SMS). It has grown beyond alphanumeric text to include multimedia messages (known as MMS) containing digital images, videos, and sound content, as well as ideograms known as emoji (happy faces and other icons). As of 2017, text messages are used by youth and adults for personal, family and social purposes and in business. Governmental and non-governmental organizations use text messaging for communication between colleagues. As with emailing, in the 2010s, the sending of short informal messages has become an accepted part of many cultures.[1] This makes texting a quick and easy way to communicate with friends and colleagues, including in contexts where a call would be impolite or inappropriate (e.g., calling very late at night or when one knows the other person is busy with family or work activities). Like e-mail and voice mail, and unlike calls (in which the caller hopes to speak directly with the recipient), texting does not require the caller and recipient to both be free at the same moment; this permits communication even between busy individuals. Text messages can also be used to interact with automated systems, for example, to order products or services from e-commerce websites, or to participate in online contests. Advertisers and service providers use direct text marketing to send messages to mobile users about promotions, payment due dates, and other notifications instead of using postal mail, email, or voicemail."


    summaries = Summarize(title, text)
    print(summaries)

    return summaries
