﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// 
// This source code was auto-generated by xsd, Version=4.8.3928.0.
// 
namespace UnitTest {
	using System.Xml.Serialization;
	
	
	/// <remarks/>
	[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
	[System.SerializableAttribute()]
	[System.Diagnostics.DebuggerStepThroughAttribute()]
	[System.ComponentModel.DesignerCategoryAttribute("code")]
	[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
	[System.Xml.Serialization.XmlRootAttribute("memory-map", Namespace="", IsNullable=false)]
	public partial class memorymap {
		
		private memory[] memoryField;
		
		private string versionField;
		
		public memorymap() {
			this.versionField = "1.0.0";
		}
		
		/// <remarks/>
		[System.Xml.Serialization.XmlElementAttribute("memory")]
		public memory[] memory {
			get {
				return this.memoryField;
			}
			set {
				this.memoryField = value;
			}
		}
		
		/// <remarks/>
		[System.Xml.Serialization.XmlAttributeAttribute()]
		public string version {
			get {
				return this.versionField;
			}
			set {
				this.versionField = value;
			}
		}
	}
	
	/// <remarks/>
	[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
	[System.SerializableAttribute()]
	[System.Diagnostics.DebuggerStepThroughAttribute()]
	[System.ComponentModel.DesignerCategoryAttribute("code")]
	[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
	[System.Xml.Serialization.XmlRootAttribute(Namespace="", IsNullable=false)]
	public partial class memory {
		
		private property[] propertyField;
		
		private memoryType typeField;
		
		private string startField;
		
		private string lengthField;
		
		/// <remarks/>
		[System.Xml.Serialization.XmlElementAttribute("property")]
		public property[] property {
			get {
				return this.propertyField;
			}
			set {
				this.propertyField = value;
			}
		}
		
		/// <remarks/>
		[System.Xml.Serialization.XmlAttributeAttribute()]
		public memoryType type {
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
	}
	
	/// <remarks/>
	[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
	[System.SerializableAttribute()]
	[System.Diagnostics.DebuggerStepThroughAttribute()]
	[System.ComponentModel.DesignerCategoryAttribute("code")]
	[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
	[System.Xml.Serialization.XmlRootAttribute(Namespace="", IsNullable=false)]
	public partial class property {
		
		private property[] itemsField;
		
		private string[] textField;
		
		private propertyName nameField;
		
		/// <remarks/>
		[System.Xml.Serialization.XmlElementAttribute("property")]
		public property[] Items {
			get {
				return this.itemsField;
			}
			set {
				this.itemsField = value;
			}
		}
		
		/// <remarks/>
		[System.Xml.Serialization.XmlTextAttribute()]
		public string[] Text {
			get {
				return this.textField;
			}
			set {
				this.textField = value;
			}
		}
		
		/// <remarks/>
		[System.Xml.Serialization.XmlAttributeAttribute()]
		public propertyName name {
			get {
				return this.nameField;
			}
			set {
				this.nameField = value;
			}
		}
	}
	
	/// <remarks/>
	[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
	[System.SerializableAttribute()]
	[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
	public enum propertyName {
		
		/// <remarks/>
		blocksize,
	}
	
	/// <remarks/>
	[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.8.3928.0")]
	[System.SerializableAttribute()]
	[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true)]
	public enum memoryType {
		
		/// <remarks/>
		ram,

		/// <remarks/>
		fram,

		/// <remarks/>
		rom,
		
		/// <remarks/>
		flash,
	}
}
