export default class Status {
    constructor(
        public connected: boolean,
        public id: string,
        public ip: string,
        public ssid: string,
    ) { }

    static fromJson(json: any): Status {
        return new Status(
            json["connected"] == 1,
            json["id"],
            json["ip"],
            json["ssid"],
        );
    }
}