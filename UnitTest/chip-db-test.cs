﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System.Xml.Serialization;

// 
// This source code was auto-generated by xsd, Version=4.8.3928.0.
// 


/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
[System.Xml.Serialization.XmlRootAttribute("chip-db-test", Namespace="", IsNullable=false)]
public partial class chipdbtest {
    
    private chipdbtestChip[] chipField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("chip")]
    public chipdbtestChip[] chip {
        get {
            return this.chipField;
        }
        set {
            this.chipField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
public partial class chipdbtestChip {
    
    private chipdbtestChipMemory[] memorymapField;
    
    private chipdbtestChipRegister[] testregistersField;
    
    private string nameField;
    
    private bool infoaField;
    
    private bool infoaFieldSpecified;
    
    private bool tlv_conflictField;
    
    private bool tlv_conflictFieldSpecified;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlArrayAttribute("memory-map")]
    [System.Xml.Serialization.XmlArrayItemAttribute("memory", IsNullable=false)]
    public chipdbtestChipMemory[] memorymap {
        get {
            return this.memorymapField;
        }
        set {
            this.memorymapField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlArrayAttribute("test-registers")]
    [System.Xml.Serialization.XmlArrayItemAttribute("register", IsNullable=false)]
    public chipdbtestChipRegister[] testregisters {
        get {
            return this.testregistersField;
        }
        set {
            this.testregistersField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string name {
        get {
            return this.nameField;
        }
        set {
            this.nameField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public bool infoa {
        get {
            return this.infoaField;
        }
        set {
            this.infoaField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlIgnoreAttribute()]
    public bool infoaSpecified {
        get {
            return this.infoaFieldSpecified;
        }
        set {
            this.infoaFieldSpecified = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public bool tlv_conflict {
        get {
            return this.tlv_conflictField;
        }
        set {
            this.tlv_conflictField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlIgnoreAttribute()]
    public bool tlv_conflictSpecified {
        get {
            return this.tlv_conflictFieldSpecified;
        }
        set {
            this.tlv_conflictFieldSpecified = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
public partial class chipdbtestChipMemory {
    
    private chipdbtestChipMemoryProperty propertyField;
    
    private MemoryTypeType typeField;
    
    private string startField;
    
    private string lengthField;
    
    private bool infoField;
    
    private bool infoFieldSpecified;
    
    /// <remarks/>
    public chipdbtestChipMemoryProperty property {
        get {
            return this.propertyField;
        }
        set {
            this.propertyField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public MemoryTypeType type {
        get {
            return this.typeField;
        }
        set {
            this.typeField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string start {
        get {
            return this.startField;
        }
        set {
            this.startField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string length {
        get {
            return this.lengthField;
        }
        set {
            this.lengthField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public bool info {
        get {
            return this.infoField;
        }
        set {
            this.infoField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlIgnoreAttribute()]
    public bool infoSpecified {
        get {
            return this.infoFieldSpecified;
        }
        set {
            this.infoFieldSpecified = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
public partial class chipdbtestChipMemoryProperty {
    
    private string nameField;
    
    private string valueField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string name {
        get {
            return this.nameField;
        }
        set {
            this.nameField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string Value {
        get {
            return this.valueField;
        }
        set {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
[System.SerializableAttribute()]
public enum MemoryTypeType {
    
    /// <remarks/>
    ram,
    
    /// <remarks/>
    fram,
    
    /// <remarks/>
    rom,
    
    /// <remarks/>
    flash,
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
public partial class chipdbtestChipRegister {
    
    private string nameField;
    
    private string startField;
    
    private string valueField;
    
    private RegBusType busField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string name {
        get {
            return this.nameField;
        }
        set {
            this.nameField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string start {
        get {
            return this.startField;
        }
        set {
            this.startField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string value {
        get {
            return this.valueField;
        }
        set {
            this.valueField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public RegBusType bus {
        get {
            return this.busField;
        }
        set {
            this.busField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
[System.SerializableAttribute()]
public enum RegBusType {
    
    /// <remarks/>
    [System.Xml.Serialization.XmlEnumAttribute("8bit")]
    Item8bit,
    
    /// <remarks/>
    [System.Xml.Serialization.XmlEnumAttribute("16bit")]
    Item16bit,
    
    /// <remarks/>
    both,
}
