package nl.jacobs.scala

object PhilsStuff {
  case class Url(protocol: String, host: String)
  
  
  trait Yes
  trait No
  
  case class UrlBuilder[Protocol, Host](protocol: Option[String] = None, host: Option[String]=None){
     def withProtocol[Host](protocol: String)(implicit ev: Protocol =:= No): UrlBuilder[Yes, Host] = UrlBuilder(Some(protocol), host);
  def withHost[Protocol](host: String)(implicit ev: Host =:= No): UrlBuilder[Protocol,Yes] = UrlBuilder(protocol, Some(host));
  def build(implicit ev1: Host =:= Yes, ev2: Protocol =:= Yes) = Url
  }
  
  UrlBuilder[No,No]().withProtocol("Http://")//.withProtocol("asd"   );
  
  case class Currency(name: String){
    case class Money(amount: Int){
      def add(other: Money) = ???
    }
  }
  
  val euro = Currency(" euro" );
  val dollars = Currency(" dollar" );
  
  val e1= euro.Money(1);
  val e2= euro.Money(1);
  val d1= dollars.Money(1);
  val d2= dollars.Money(1);
  
  e1.add(e2)
  d1.add(d2)
  
  e1.add(d1)
}