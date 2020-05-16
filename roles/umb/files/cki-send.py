#!/usr/bin/python3

import argparse
import json
import stomp


def main(args):
    hosts = [(args.broker, args.port)]
    conn = stomp.StompConnection12(host_and_ports=hosts,
                                   use_ssl=True,
                                   ssl_key_file=args.ssl_key_file,
                                   ssl_cert_file=args.ssl_cert_file)
    conn.connect(wait=True)

    msg = {
        "cki_pipeline_id": args.pipeline_id,
        "summarized_result": args.result,
        "team_email": "3rd-qe-list@redhat.com",
        "team_name": "Virt-QE-S1",
        "results": [
            {
                "test_name": "LTP_Lite",
                "test_description": "Cloud platform - {}".format(args.cloud),
                "test_arch": args.arch,
                "test_result": args.result,
                "test_log_url": [
                    args.log_url
                ],
                "test_waived": "True"
            }
        ]
    }
    msg_json = json.dumps(msg)
    print(msg_json)
    conn.send("/topic/VirtualTopic.eng.cki.results", body=msg_json)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send result to VirtualTopic.eng.cki.results')
    parser.add_argument("--broker", type=str, required=True, help="ActiveMQ Broker hostname")
    parser.add_argument("--port", type=int, required=True, help="Stomp port")
    parser.add_argument("--ssl_cert_file", type=str, required=True, help="Certification file")
    parser.add_argument("--ssl_key_file", type=str, required=True, help="Private key file")
    parser.add_argument("--pipeline_id", type=int, required=True, help="CKI pipeline ID")
    parser.add_argument("--arch", type=str, required=True, help="Test arch")
    parser.add_argument("--log_url", type=str, required=True, help="Test log URL")
    parser.add_argument("--result", type=str, required=True, help="Test result")
    parser.add_argument("--cloud", type=str, required=True, help="Cloud platform")
    args = parser.parse_args()

    main(args)
