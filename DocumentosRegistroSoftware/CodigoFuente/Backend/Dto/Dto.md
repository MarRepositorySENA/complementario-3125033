```
//DTO PERMISOSDTO

package com.persona.Backend.Dto.Security;

public interface PermisosDto {
	
  String getVistaRuta();
  String getVistaNombre();
  String getModuloRuta();
  String getModuloNombre();
  String getIcono();
  String getRol();
  String getPersonaNombre();
  Long   getPadreId();
  
}


//DTO DATASELECTDTO

package com.persona.Backend.Dto;

public interface DataSelectDto
{
     Long getId();
    String getTextoMostrar();
}

//DTO IDATOSUSUARIODTO
package com.persona.Backend.Dto;

public interface IDatosUsuarioDto {

	String getPrimerNombre();
	String getSegundoNombre();
	String getTipoDocumento();
	String getNumeroDocumento();
	String getTelefono();
	String getEmail();
	String getUsuario();
	
}
//DTO ILOGINDTO
package com.persona.Backend.Dto;

public interface ILoginDto {

	Long getUserId();
	Boolean getState();
	String getUsuarioNombre();
	String getContrasenia();
	Integer getQuantity();
	
	
}
//DTO IVALIDARDATOS
package com.persona.Backend.Dto;

public interface IValidarDatosUsuarioDto {

	Integer getCantidad();
	
}




```