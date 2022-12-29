import Status from "../models/status";

const root: string = `http://${window.location.hostname}`;

export default class Api {
    async getStatus(): Promise<Status> {
        const res = await fetch(`${root}/api/status`);
        this.checkResponse(res);

        const json = await res.json();

        return Status.fromJson(json);
    }

    async connect(ssid: string, pass: string) {
        const res = await fetch(`${root}/connect?ssid=${ssid}&pass=${pass}`);
        this.checkResponse(res);
    }

    async disconnect() {
        const res = await fetch(`${root}/disconnect`);
        this.checkResponse(res);
    }

    checkResponse(res: Response, msg?: string) {
        if (!res.ok) {
            throw Error(msg ?? `Error! Status code: ${res.status}, ul: ${res.url}`);
        }
    }
}