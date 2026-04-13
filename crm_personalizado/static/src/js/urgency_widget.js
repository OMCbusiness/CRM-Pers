/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useRecordObserver } from "@web/model/relational_model/utils";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

const URGENCY_LABELS = {
    1: "Muy baja",
    2: "Baja",
    3: "Media",
    4: "Alta",
    5: "Máxima",
};

export class UrgencyStarsWidget extends Component {
    static template = "crm_personalizado.UrgencyStarsWidget";
    static props = {
        ...standardFieldProps,
    };

    get value() {
        return this.props.record.data[this.props.name] || 1;
    }

    getLabel(level) {
        return URGENCY_LABELS[level] || "";
    }

    getCurrentLabel() {
        return URGENCY_LABELS[this.value] || "";
    }

    setValue(level) {
        if (!this.props.readonly) {
            this.props.record.update({ [this.props.name]: level });
        }
    }
}

registry.category("fields").add("urgency_stars", {
    component: UrgencyStarsWidget,
    displayName: "Urgency Stars",
    supportedTypes: ["integer"],
});
